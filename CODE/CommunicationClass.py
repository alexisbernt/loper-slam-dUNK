# This will be the communication class
# Dylan will begin coding the communication
import tkinter as tk
from tkinter import Label


class Communication:
    def __init__(self):
        self.window = tk.Tk()
        self.on_screen = []

    def reset_for_communicate(self):
        # Clear The Screen_________
        for item in self.on_screen:
            item.pack_forget()
        self.on_screen = []
        # Title____________________________________________________________
        communication_title = Label(self.window, text="COMMUNICATE", font=("litera", 25), pady=10)
        self.on_screen.append(communication_title)
        communication_title.pack()

# run_com_instance = Communication()
# run_com_instance.reset_for_communicate()
