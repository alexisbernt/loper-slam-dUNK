import tkinter as tk
from datetime import date
from functools import partial
from ttkbootstrap import Style
from tkinter import Label, Button
# Will import the classes to connect to the GUI
from RandomizerClass import RandomClass
from CommunicationClass import Communication
from CalendarClass import Calendar

from Table_Events import EventsController
from Table_Athletes import AthletesController
from Table_Coaches import CoachesController

# Ideas to clear the screen (so we can put everything on the same screen)
# I made a self.on_screen = [] list and that is how we will control
# what is on the screen at each time. To put something on the screen, append to the list

class SlamdUNK:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("loperslamdUNK")
        self.window.geometry(f'{self.window.winfo_screenwidth() // 2}x{self.window.winfo_screenheight() // 1.5:.0f}')
        self.on_screen = []
        self.notes = []
        self.user_type = 0
        self.tempInt = tk.IntVar()
        self.sign_in_screen()
        self.window.mainloop()

    # Clear The Screen Functionalities
    def clear_screen(self):
        for widget in self.on_screen:
            widget.destroy()

    def clear_notes(self):
        for widget in self.notes:
            widget.destroy()
        # for item in self.on_screen:
        #     item.pack_forget()

    def select_user_type(self):
        self.user_type = self.tempInt.get()
        print(self.user_type)

    def sign_in_screen(self):
        self.communication = Communication(self.window,self.on_screen)  # We need commmunication w/ SQL Server right away to get username / password info

        self.clear_screen()
        self.clear_notes()
        sign_in_page_title = Label(self.window, text="Welcome to loperslamdUNK!", font=("Ariel", 28), pady=10)
        self.on_screen.append(sign_in_page_title)
        sign_in_page_title.pack()
        # FOR USERS TO SIGN IN
        self.tempInt = tk.IntVar()
        R1 = tk.Radiobutton(self.window, text="Athlete Login", font=("Ariel", 18), variable=self.tempInt, value=1,
                        command=self.select_user_type)
        self.on_screen.append(R1)
        R1.pack()

        R2 = tk.Radiobutton(self.window, text="Coach Login", font=("Ariel", 18), variable=self.tempInt, value=2,
                        command=self.select_user_type)
        self.on_screen.append(R2)
        R2.pack()

        username_label = Label(self.window, text="Enter username", font=("Ariel", 18))
        self.on_screen.append(username_label)
        username_label.pack()
        username_entry = tk.Entry(self.window)
        self.on_screen.append(username_entry)
        username_entry.pack()
        password_label = Label(self.window, text="Enter password", font=("Ariel", 18))
        self.on_screen.append(password_label)
        password_label.pack()
        password_entry = tk.Entry(self.window, show="*")
        self.on_screen.append(password_entry)
        password_entry.pack()


        login_button = Button(self.window, text="Login", font=("Ariel", 15),
                              command=lambda: self.login(username_entry.get(), password_entry.get()))
        self.on_screen.append(login_button)
        login_button.pack()

    def login(self, username, password):
        # Right now going straight to dashboard screen
        # Instead hook it up, so it checks to see if username and password
        # are valid (in database). If so, login, else error.
        # LOGIC ----------------------------

        if self.user_type == 1:
            #athlete login...
            athleteC = AthletesController(self.communication.cnxn)
            result = athleteC.checkLogin(username, password)
            if result != True:
                return False
        elif self.user_type == 2:
            coachC = CoachesController(self.communication.cnxn)
            result = coachC.checkLogin(username, password)
            if result != True:
                return False
        else:
            return False
        print("Login successful!")
        # if name = valid:
        self.dashboard_screen()
        self.addCalendarEvents()
        # else:
        # messagebox error
    def do_communicate(self):
        self.clear_screen()
        self.clear_notes()
        self.communication.reset_for_communicate()
        self.back_button()

    def dashboard_screen(self):
        # RIGHT NOW I HAVE COMMENTED COMMUNICATION CLASS OUT ----------------------------
        # I have commented out some classes that are connected to the SQL database
        # That functionality still needs to be implemented/connected
        # self.communication = Communication()  # create instance of the class
        # RIGHT NOW I HAVE COMMENTED CALENDAR CLASS OUT ----------------------------
        currentDate = date.today()
        self.calendar = Calendar(currentDate.year, currentDate.month,self.communication.cnxn)        # create instance of the class
        self.random = RandomClass()  # create instance of the class
        # Clear The Screen all over again
        self.clear_screen()
        self.clear_notes()
        # Title
        dashboard_title = Label(self.window, text="DASHBOARD", font=("litera", 25), pady=10)
        self.on_screen.append(dashboard_title)
        dashboard_title.pack()
        # You can use the command: command=lambda: self.[call class].[call function]() to connect the button
        # Buttons for navigating to different pages w/n the application
        communication_button = Button(self.window, text="COMMUNICATE", font=("Ariel", 15),
                                      command=lambda: self.do_communicate())
        self.on_screen.append(communication_button)
        communication_button.pack()
        random_button = Button(self.window, text="RANDOM", font=("Ariel", 15),
                               command=lambda: self.run_random())
        self.on_screen.append(random_button)
        random_button.pack()
        calendar_button = Button(self.window, text="CALENDAR", font=("Ariel", 15), command=lambda: self.calendar.show())
        self.on_screen.append(calendar_button)
        calendar_button.pack()

    # WE NEED A BACK BUTTON STILL 
    def back_button(self):
        button_back = tk.Button(self.window, text="Back", font=("Ariel", 15), command=self.go_back)
        self.on_screen.append(button_back)
        button_back.pack()

    def go_back(self):
        self.clear_screen()
        self.clear_notes()
        self.dashboard_screen()

    def addCalendarEvents(self):
        events = EventsController(self.communication.cnxn)
        currentDate = date.today()
        month_events = events.getMonthEvents(currentDate.month, currentDate.year)  # Change the year and month as needed

        self.calendar.addMultipleEvents(month_events)

    # MUST CREATE THE FUNCTIONS WITH THE BUTTONS WITHIN THIS SCRIPT ------------
    # I just copied my "reset for random code" from my randomizer class and pasted it in a new function on loperslamdUNK.py
    def run_random(self):
        # Resets the screen for functionality to happen
        self.clear_screen()
        self.clear_notes()
        # Title____________________________________________________________
        random_title = Label(self.window, text="RANDOM", font=("litera", 25), pady=10)
        self.on_screen.append(random_title)
        random_title.pack()
        # --- Commented this out, it was causing errors with clear screen and doesn't appear to do anything
        # self.on_screen.append(RandomClass.add_name)
        name_entry = self.random.add_name(self.window)
        self.on_screen.append(name_entry)
        name_list = tk.Listbox(self.window, selectmode=tk.SINGLE, height=10, width=30)
        name_to_list_partial = partial(self.random.add_name_to_list, name_entry, name_list)
        # Researched lambda: In Python, lambda is a keyword used to create anonymous functions
        add_button = tk.Button(self.window, text='ADD NAME',
                               command=lambda: self.random.add_name_to_list(name_entry, name_list))
        add_button.pack()
        self.on_screen.append(add_button)
        name_list.pack(pady=10)
        self.on_screen.append(name_list)
        name_to_random_partial = partial(self.random.select_random_name, name_to_list_partial)
        # lambda is being used to create a function that calls self.add_name_to_list(name_entry, name_list) when the
        # button is clicked
        random_button = tk.Button(self.window, text="SELECT RANDOM NAME FROM ABOVE",
                                  command=lambda: self.random.select_random_name(name_list))
        random_button.pack()
        self.on_screen.append(random_button)
        selected_name_var = tk.StringVar()
        selected_name_label = tk.Label(self.window, textvariable=selected_name_var)
        selected_name_label.pack()
        self.on_screen.append(selected_name_label)
        self.back_button()


slamdunk_instance = SlamdUNK()
