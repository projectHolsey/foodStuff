from Lists.CreateList import CreateList
from Recipes.RecipeFunctions import RecipeFuncs

def get_input():
    return input(">")


class ConsoleApp:
    def __init__(self):
        self.running = True
        pass

    def start(self):

        while self.running:
            self.user_options()

    def user_options(self):

        print("Please enter a number as input : ")

        while self.continue_polling:
            print("1. Create list")
            print("2. Edit List")
            print("3. Create Recipe")
            print("4. Edit Recipe")
            print("5. Exit")
            choice = get_int_input("Choose option > ", 1, 4)
            self.handle_choice(choice)
            print("\n\n")

        return

    def handle_choice(self, x):
        if x == 1:
            new_list = CreateList()
            return

        # Add new recipe
        if x == 2:
            for index, list in enumerate(FoodThingsGlobal.shopping_lists):
                print("{0}. {1}".format(str(index), list.name))
            choice = get_int_input("Choose option > ", 1, len(FoodThingsGlobal.shopping_lists))
            list.edit_list()

        # Remove Recipe
        if x == 3:
            new_recipe = create_and_edit_recipe()
            return

        # show all recipes
        if x == 4:
            for index, list in enumerate(FoodThingsGlobal.recipe_list):
                print("{0}. {1}".format(str(index), list.name))
            choice = get_int_input("Choose option > ", 1, len(FoodThingsGlobal.recipe_list))
            edit_recipe = RecipeFuncs(list)
            edit_recipe.edit_list()

        if x == 5:
            self.continue_polling = False
            return

    def save_and_exit(self):
         # recipes dataset
        self.running = False


