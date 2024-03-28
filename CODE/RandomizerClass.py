# This will be the randomizer class
# Alexis will begin coding the randomizer
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
    # will insert more functions here
RandomClass()