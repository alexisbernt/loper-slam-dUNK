# This will be the randomizer class
# Alexis will begin coding the randomizer
name_list = []
def select_random_name(name_list):
    if name_list.size() > 0:
        random_name = random.choice(name_list.get(0, tk.END))
        selected_name_var.set(f"Selected Name: {random_name}")
    else:
        selected_name_var.set(f"Error. No names entered.")
        print('Error. No names entered.')