# This is where the dashboard will be

# Will implement a GUI
import tkinter as tk
from ttkbootstrap import Style
from tkinter import Label, Button
# Will import the classes to connect to the GUI
from RandomizerClass import RandomClass
from CommunicationClass import Communication
from CalendarClass import Calendar
# In the classes, we should have the functionality implemented
class SlamdUNK:
    def __init__(self):
        self.window = tk.Tk()
        self.communication = Communication() # create instance of the class
        # JUAN, PLEASE CONNECT YOUR BUTTON TO YOUR LIKING HERE :)
        self.calendar = Calendar(2024, 4) # create instance of the class
        self.random = RandomClass()# create instance of the class

        self.window.title("loper slam dUNK Version 1")
        self.window.geometry(f'{self.window.winfo_screenwidth() // 2}x{self.window.winfo_screenheight() // 1.5:.0f}')
        self.on_screen = []
        self.notes = []
        # self.open_screen()
        self.style = Style(theme="litera")  # creating ttkbootstrap style with the specified theme
        self.style.theme_use('litera')
        self.dashboard_screen() # Call dashboard_screen method

    def dashboard_screen(self):
        # Clear The Screen_________
        self.clear_screen()
        self.clear_notes()
        # Title____________________________________________________________
        dashboard_title = Label(self.window, text="DASHBOARD", font=("litera", 25), pady=10)
        self.on_screen.append(dashboard_title)
        dashboard_title.pack()

        # Buttons for navigating to different pages___________________________________________________
        communication_button = Button(self.window, text="COMMUNICATE", font=("Ariel", 15),
                                command=lambda: self.communication.reset_for_communicate())
        self.on_screen.append(communication_button)
        communication_button.pack()
        random_button = Button(self.window, text="RANDOM", font=("Ariel", 15),
                                      command=lambda: self.random.reset_for_random())
        self.on_screen.append(random_button)
        random_button.pack()
        # JUAN, you can edit your button here
        # You can use the command: command=lambda: self.[call class].[call function]() to connect the button
        calendar_button = Button(self.window, text="CALENDAR", font=("Ariel", 15), command= lambda: self.calendar.show())
        self.on_screen.append(calendar_button)
        calendar_button.pack()
    def clear_screen(self):
        for item in self.on_screen:
            item.pack_forget()
        self.on_screen = []

    def clear_notes(self):
        self.notes.clear()

run_instance = SlamdUNK()
run_instance.window.mainloop()
