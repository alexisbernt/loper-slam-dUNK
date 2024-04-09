# This is where the dashboard will be

# Will implement a GUI
import tkinter as tk
from datetime import date

from ttkbootstrap import Style
from tkinter import Label, Button
# Will import the classes to connect to the GUI
from RandomizerClass import RandomClass
from CommunicationClass import Communication
from CalendarClass import Calendar
from Table_Events import EventsController

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
        self.sign_in_screen()
        self.window.mainloop()

    # Clear The Screen Functionalities
    def clear_screen(self):
        for widget in self.notes:
            widget.destroy()
    def clear_notes(self):
        for widget in self.notes:
            widget.destroy()
        # for item in self.on_screen:
        #     item.pack_forget()

    def sign_in_screen(self):
        self.clear_screen()
        self.clear_notes()
        sign_in_page_title = Label(self.window, text="Welcome to loperslamdUNK", font=("Ariel",28), pady=10)
        self.on_screen.append(sign_in_page_title)
        sign_in_page_title.pack()
        # FOR USERS TO SIGN IN
        username_label = Label(self.window, text="Enter username", font=("Ariel", 18))
        self.on_screen.append(username_label)
        username_label.pack()
        username_entry = tk.Entry(self.window)
        self.on_screen.append(username_entry)
        username_entry.pack()
        password_label = Label(self.window, text="Enter password", font=("Ariel", 18))
        self.on_screen.append(password_label)
        password_label.pack()
        password_entry = tk.Entry(self.window)
        self.on_screen.append(password_entry)
        password_entry.pack()
        login_button = Button(self.window, text="Login", font=("Ariel", 15),
                                command=lambda: self.login(username_entry.get(), password_entry.get()))
        self.on_screen.append(login_button)
        login_button.pack()

    def login(self,username, password):
        # Right now going straight to dashboard screen
        # Instead hook it up, so it checks to see if username and password
        # are valid (in database). If so, login, else error.
        self.dashboard_screen()

    def dashboard_screen(self):
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
                                command=lambda: self.communication.reset_for_communicate())
        self.on_screen.append(communication_button)
        communication_button.pack()
        random_button = Button(self.window, text="RANDOM", font=("Ariel", 15),
                                      command=lambda: self.random.reset_for_random())
        self.on_screen.append(random_button)
        random_button.pack()
        calendar_button = Button(self.window, text="CALENDAR", font=("Ariel", 15), command= lambda: self.calendar.show())
        self.on_screen.append(calendar_button)
        calendar_button.pack()

    # self.communication = Communication()  # create instance of the class
    # # JUAN, PLEASE CONNECT YOUR BUTTON TO YOUR LIKING HERE :)
    # currentDate = date.today()
    # self.calendar = Calendar(2004, 3)
    # self.random = RandomClass()  # create instance of the class
    # # self.open_screen()
    # self.style = Style(theme="litera")  # creating ttkbootstrap style with the specified theme
    # self.style.theme_use('litera')
    # self.dashboard_screen()  # Call dashboard_screen method
    # self.addCalendarEvents()

    def addCalendarEvents(self):
        events = EventsController()
        month_events = events.getMonthEvents(3, 2004)  # Change the year and month as needed
    
        self.calendar.addMultipleEvents(month_events)

# Example usage
slamdunk_instance = SlamdUNK()
# slamdunk_instance.name_entry.pack_forget()  # hide the entry widget
# slamdunk_instance.window.mainloop()
