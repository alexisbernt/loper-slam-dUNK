# This is where the dashboard will be

# Will implement a GUI

# Will import the classes to connect to the GUI
# from RandomizerClass import RandomClass
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

# Current functionality (working on putting into the class)
import tkinter as tk
from tkinter import simpledialog, StringVar
import ttkbootstrap
import random
import csv

# root window is the main window that contains all GUI elements(buttons, labels, entry widgets, etc.)
root = tk.Tk()
# result_var = StringVar()
root.geometry("400x600")
root.title("loper slam dUNK Version 1")


def add_name():  # add the name
    name = name_entry.get()
    if name:
        name_list.insert(tk.END, name)
        name_entry.delete(0, tk.END)


def clear_names():
    name_list.delete(0, tk.END)


def select_random_name():
    if name_list.size() > 0:
        random_name = random.choice(name_list.get(0, tk.END))
        selected_name_var.set(f"Selected Name: {random_name}")
    else:
        selected_name_var.set(f"Error. No names entered.")
        print('Error. No names entered.')


def names_library():
    # a function to store remember names that were entered in the past
    csv_file_path = "names.csv"
    # Write the list to a CSV file
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stored Names"])  # Optional: Write a header row
        for name in name_list.get(0, tk.END):
            writer.writerow([name])


def get_names_library():
    # Working here to get last stored names from csv file to display back on page
    file = open('names.csv')
    type(file)
    rows = []
    with (open('names.csv', mode="r", newline="") as file):
        csvreader = csv.reader(file)
        header = next(csvreader)  # Optional: Read the header row
        for row in csvreader:
            rows.append(row)
            if row:  # display past list
                name_list.insert(tk.END, row)
                name_entry.delete(0, tk.END)
    # getting header and row to display in the terminal
    # print(header)
    # print(rows)

label = tk.Label(root, text="welcome to loper slam dUNK!", font=('Helvetica', 16), fg=('yellow'))
label.pack(pady=20)  # to change the text color of the label use the fg (foreground) option
# To add names
name_entry = tk.Entry(root, width=30)  # entry widget for name input
name_entry.pack(pady=10)
add_button = tk.Button(root, text="ADD NAME", command=add_name)
add_button.pack()
spacing3 = tk.Label(root, text=" ")
spacing3.pack(pady=0.5)
# To list the names
name_list = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=30)
name_list.pack(pady=10)
# "Clear Names" button
clear_button = tk.Button(root, text="CLEAR NAMES ABOVE", command=clear_names)
clear_button.pack()
spacing4 = tk.Label(root, text=" ")
spacing4.pack(pady=0.5)
# "Select Random Name" button
random_button = tk.Button(root, text="SELECT RANDOM NAME FROM ABOVE", command=select_random_name)
random_button.pack()
# Create a label to display the selected random name
selected_name_var = tk.StringVar()
selected_name_label = tk.Label(root, textvariable=selected_name_var)
selected_name_label.pack()
# Remembering the list entered to store into names_library
remember_button = tk.Button(root, text="REMEMBER CURRENT LIST DISPLAYED", command=names_library)
remember_button.pack()
spacing1 = tk.Label(root, text=" ")
spacing1.pack(pady=0.5)
# Pull up past (the last stored) names_library entered names
get_stored_button = tk.Button(root, text="GET LAST STORED NAMES", command=get_names_library)
get_stored_button.pack()
spacing2 = tk.Label(root, text=" ")
spacing2.pack(pady=0.5)
# Result variable
result_var = StringVar()

# Start the main loop
root.mainloop()