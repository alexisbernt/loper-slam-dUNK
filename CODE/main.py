# This is where the dashboard will be

# Will implement a GUI
import tkinter as tk
from tkinter import simpledialog, StringVar
# from ttkbootstrap import Style
import random
import csv

# Will import the classes to connect to the GUI
from RandomizerClass import RandomClass
# In the classes, we should have the functionality implemented
class SlamdUNK:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("loper slam dUNK Version 1")
        self.window.geometry(f'{self.window.winfo_screenwidth() // 2}x{self.window.winfo_screenheight() // 1.5:.0f}')
        self.on_screen = []
        self.notes = []
        # self.open_screen()
        # self.style = Style(theme="litera")  # creating ttkbootstrap style with the specified theme
        # self.style.theme_use('litera')
        self.window.mainloop()

    def clear_screen(self):
        for widget in self.on_screen:
            widget.destroy()

SlamdUNK()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
