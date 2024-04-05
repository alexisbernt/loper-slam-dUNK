# This will be the randomizer class
# Alexis will begin coding the randomizer

# This script currently does NOT run ... I am working on putting the functions from the
# main.py script into a class in this .py script
import tkinter as tk
from tkinter import Label
import random
from functools import partial


class RandomClass:
    # init method initializes if the coach wants to do a single selection
    # or select multiple members / group multiple members together from a team
    def __init__(self):
        self.window = tk.Tk()
        self.__name_list = []
        self.on_screen = []

    def add_name(self, root):  # add the name
        # To add names
        name_entry = tk.Entry(root, width=30)  # entry widget for name input
        name_entry.pack(pady=10)
        return name_entry

    def add_name_to_list(self, name_entry, name_list):
        # name_entry, name_list = self.add_name(self.window)
        if name_entry:
            name_list.insert(tk.END, name_entry.get())
            name_entry.delete(0, tk.END)

    def select_random_name(self, names_from_list, selected_name_var=None):
        if selected_name_var is None:
            selected_name_var = tk.StringVar()
        if names_from_list.size() > 0:
            random_name = random.choice(names_from_list.get(0, tk.END))
            selected_name_var.set(f"Selected Name: {random_name}")
        else:
            selected_name_var.set(f"Error. No names entered.")
            print('Error. No names entered.')

    def reset_for_random(self):
        self.on_screen = []
        # Title____________________________________________________________
        random_title = Label(self.window, text="RANDOM", font=("litera", 25), pady=10)
        self.on_screen.append(random_title)
        random_title.pack()
        self.on_screen.append(RandomClass.add_name)
        name_entry = self.add_name(self.window)  # store the name_entry widget
        self.on_screen.append(name_entry)
        name_list = tk.Listbox(self.window, selectmode=tk.SINGLE, height=10, width=30)
        name_to_list_partial = partial(self.add_name_to_list, name_entry, name_list)
        add_button = tk.Button(self.window, text='ADD NAME', command=name_to_list_partial)
        add_button.pack()
        self.on_screen.append(add_button)
        name_list.pack(pady=10)
        self.on_screen.append(name_list)
        name_to_random_partial = partial(self.select_random_name, name_list)
        random_button = tk.Button(self.window, text="SELECT RANDOM NAME FROM ABOVE", command=name_to_random_partial)
        random_button.pack()
        self.on_screen.append(random_button)
        selected_name_var = tk.StringVar()  # Create a label to display the selected random name
        selected_name_label = tk.Label(self.window, textvariable=selected_name_var)
        selected_name_label.pack()
        self.on_screen.append(selected_name_label)
    #
    #

    #
    #
    # def clear_names():
    #     name_list.delete(0, tk.END)
    #

    # def names_library():
    #     # a function to store remember names that were entered in the past
    #     csv_file_path = "names.csv"
    #     # Write the list to a CSV file
    #     with open(csv_file_path, mode="w", newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["Stored Names"])  # Optional: Write a header row
    #         for name in name_list.get(0, tk.END):
    #             writer.writerow([name])
    #
    #
    # def get_names_library():
    #     # Working here to get last stored names from csv file to display back on page
    #     file = open('names.csv')
    #     type(file)
    #     rows = []
    #     with (open('names.csv', mode="r", newline="") as file):
    #         csvreader = csv.reader(file)
    #         header = next(csvreader)  # Optional: Read the header row
    #         for row in csvreader:
    #             rows.append(row)
    #             if row:  # display past list
    #                 name_list.insert(tk.END, row)
    #                 name_entry.delete(0, tk.END)
    #     # getting header and row to display in the terminal
    #     # print(header)
    #     # print(rows)
    #
    #
    # label = tk.Label(root, text="welcome to loper slam dUNK!", font=('Helvetica', 16), fg=('yellow'))
    # label.pack(pady=20)  # to change the text color of the label use the fg (foreground) option

    # spacing3.pack(pady=0.5)

    # # "Clear Names" button
    # clear_button = tk.Button(root, text="CLEAR NAMES ABOVE", command=clear_names)
    # clear_button.pack()
    # spacing4 = tk.Label(root, text=" ")
    # spacing4.pack(pady=0.5)

    # # Remembering the list entered to store into names_library
    # remember_button = tk.Button(root, text="REMEMBER CURRENT LIST DISPLAYED", command=names_library)
    # remember_button.pack()
    # spacing1 = tk.Label(root, text=" ")
    # spacing1.pack(pady=0.5)
    # # Pull up past (the last stored) names_library entered names
    # get_stored_button = tk.Button(root, text="GET LAST STORED NAMES", command=get_names_library)
    # get_stored_button.pack()
    # spacing2 = tk.Label(root, text=" ")
    # spacing2.pack(pady=0.5)
    # # Result variable
    # result_var = StringVar()


RandomClass()
