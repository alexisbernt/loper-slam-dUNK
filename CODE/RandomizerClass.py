# This will be the randomizer class
# Alexis will begin coding the randomizer

# This script currently does NOT run ... I am working on putting the functions from the
# main.py script into a class in this .py script
import random
class RandomClass:
# init method initializes if the coach wants to do a single selection
# or select multiple members / group multiple members together from a team
    def __init__(self, group_selection, single_selection):
        self.__group_selection = group_selection
        self.__single_selection = single_selection
    name_list = []
    def select_random_name(name_list):
        if name_list.size() > 0:
            random_name = random.choice(name_list.get(0, tk.END))
            selected_name_var.set(f"Selected Name: {random_name}")
        else:
            selected_name_var.set(f"Error. No names entered.")
            print('Error. No names entered.')


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
RandomClass()