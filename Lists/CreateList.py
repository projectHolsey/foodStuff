from Lists.ListObj import ListObj
from application.FoodThingsGlobal import FoodThingsGlobal
from Recipes.RecipeFunctions import RecipeFuncs


def get_int_input(prompt, lower, upper):
    while True:
        try:
            weight = int(input(prompt))
            if lower <= weight <= upper:
               return weight
        except:
            print("That's not a valid input!")


class CreateList:
    def __init__(self):
        self.list = None
        self.continue_polling = True
        pass

    def create_new_list(self):
        name = input("Please enter a name for the List : ")
        self.list = ListObj()
        self.list.name = name

        while self.continue_polling:
            print("1. Add Recipe")
            print("2. Remove Recipe")
            print("3. Show all Recipes")
            print("4. Show list ingredients")
            print("5. Show list recipes macros (short)")
            print("6. Save list")
            choice = get_int_input("Choose option > ", 1, 6)
            self.handle_choice(choice)
            print("\n\n")

        recipe = self.list
        self.list = None
        self.continue_polling = True
        return recipe

    def handle_choice(self, x):
        if x == 0:
            self.continue_polling = False
            return

        # Add new recipe
        if x == 1:
            for index, item in enumerate(FoodThingsGlobal.recipe_list):
                print(index, item.name)
            choice = get_int_input("Enter index of recipe > ", 0, len(FoodThingsGlobal.recipe_list))

            self.list.recipes_list.append(FoodThingsGlobal.recipe_list[choice])

        # Remove Recipe
        if x == 2:
            for index, item in enumerate(self.list.recipes_list):
                print(index, item.name)
            choice = get_int_input("Enter index of recipe > ", 0, len(self.list.recipes_list))

            self.list.recipes_list.remove([choice])

        # show all recipes
        if x == 3:
            for index, item in enumerate(self.list.recipes_list):
                print(index, item.name)

        # show ingredients list
        if x == 4:
            ingredient_and_quantities = {}
            for index, item in enumerate(self.list.recipes_list):
                recipe = RecipeFuncs(item)

                x = recipe.return_all_ingredient_names_n_quantities()

                for key, value in x:
                    if key in ingredient_and_quantities.keys():
                        ingredient_and_quantities[key] = int(ingredient_and_quantities[key]) + int(value)
                    else:
                        ingredient_and_quantities[key] = value

            for key, value in ingredient_and_quantities:
                print("{0} x {1}".format(key, value))

        # show list and macros
        if x == 5:
            totals = {}
            ingredient_and_quantities = {}
            for index, item in enumerate(self.list.recipes_list):
                recipe = RecipeFuncs(item)

                y = recipe.get_recipe_total_macros_short()
                x = recipe.return_all_ingredient_names_n_quantities()

                for key, value in y:
                    if key in totals.keys():
                        totals[key] = int(totals[key]) + int(value)
                    else:
                        totals[key] = value

                for key, value in x:
                    if key in ingredient_and_quantities.keys():
                        ingredient_and_quantities[key] = int(ingredient_and_quantities[key]) + int(value)
                    else:
                        ingredient_and_quantities[key] = value

            for key, value in ingredient_and_quantities:
                print("{0} x {1}".format(key, value))

            print(totals)

        # Save list
        if x == 6:
            FoodThingsGlobal.shopping_lists.append(self.list)
            self.continue_polling = False
