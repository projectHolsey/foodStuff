import timeit
import logging
from Foods.IngredientFunctions import find_ingredient, find_weight_multiplier, find_potential_ingredients
from Foods.IngredientObj import IngredientObj
from Recipes.RecipeObj import RecipeObj
from OnStart.LoadIngredients import load_ingredient
from application.FoodThingsGlobal import FoodThingsGlobal


def get_int_input(prompt, lower, upper):
    while True:
        try:
            weight = int(input(prompt))
            if lower <= weight <= upper:
               return weight
        except:
            print("That's not a valid input!")


class RecipeFuncs:

    def __init__(self, recipe_obj=None):
        self.recipe = recipe_obj if recipe_obj else None
        self.continue_polling = True

    def create_and_edit_recipe(self, ):

        if not self.recipe:
            name = input("Please enter a name for the recipe : ")
            self.recipe = RecipeObj()
            self.recipe.name = name

        while self.continue_polling:
            print("1. Add Ingredient")
            print("2. Edit Ingredient weight")
            print("3. Edit Ingredient quantity")
            print("4. Remove Ingredient")
            print("5. Show current Ingredients and macros")
            print("6. Show current recipe ingredients and quantities")
            print("7. Show current recipe macros (short)")
            print("8. Save recipe")
            choice = get_int_input("Choose option > ", 1, 8)
            self.handle_choice(choice)
            print("\n\n")

        recipe = self.recipe
        self.recipe = None
        self.continue_polling = True
        return recipe

    def handle_choice(self,x):
        if x == 0:
            self.continue_polling = False
            return

        # Add new ingredient
        if x == 1:
            ingredient = input("Enter new Ingredient name > ")
            quantity = get_int_input("Enter quantity > ", 1, 9999999)

            if self.attempt_add_ingredient(ingredient, quantity):
                print("Ingredient added! \n")
                return
            else:
                potential_ingredients = find_potential_ingredients(ingredient)
                if len(potential_ingredients) == 0:
                    print("Could not find any ingredient : " + str(ingredient))
                    return
                else:
                    for index, item in enumerate(potential_ingredients):
                        print(str(index), str(item.name))
                    ingredient_choice = get_int_input("Enter index for choice > ", 0, len(potential_ingredients))

                    if self.attempt_add_ingredient(potential_ingredients[ingredient_choice], quantity):
                        print("Ingredient added! \n")
            return

        # Edit an ingredient
        if x == 2:
            for index, item in enumerate(self.recipe.ingredients_list):
                print(str(index), item.name)
            ingredient = get_int_input("Enter index of ingredient to edit > ", 0, len(self.recipe.ingredients_list))

            self.change_ingredient_weight(ingredient)
            return

        # Edit quantity
        if x == 3:
            item_names = []
            counter = 0
            for name, quantity in self.recipe.quantities.items():
                print(str(counter) + ". " + str(name) + " x" + str(quantity))
                item_names.append(str(name))
                counter += 1
            index = get_int_input("Enter index of item to change > ", 0, len(item_names))
            new_quantity = get_int_input("Enter new quantity > ", 1, 9999999)
            print(f"Quantity of {item_names[index]} changed from {self.recipe.quantities[item_names[index]]} to {new_quantity}")
            self.recipe.quantities[item_names[index]] = int(new_quantity)
            return

        # remove ingredient
        if x == 4:
            for index, item in enumerate(self.recipe.ingredients_list):
                print(str(index), item.name)
            ingredient = get_int_input("enter index of ingredient > ", 0, len(self.recipe.ingredients_list))
            self.remove_ingredient(self.recipe.ingredients_list[ingredient])
            return

        # Show current ingredients and macros
        if x == 5:
            for index, item in enumerate(self.recipe.ingredients_list):
                print(str(index), item.name)
            index = get_int_input("enter index of ingredient > ", 0, len(self.recipe.ingredients_list))
            self.display_ingredient_macros(index)
            return

        # Show current recipe ingredients and quantities
        if x == 6:
            for name, quantity in self.recipe.quantities.items():
                print(str(quantity) + " x " + str(name))

        # Show current recipe total macros
        if x == 7:
            self.display_recipe_macros()

        # save recipe
        if x == 8:
            self.save_recipe()

    def attempt_add_ingredient(self, ingredient, quantity):
        """
        Add an ingredient if it's name is exact to any ingredient in list
        :param ingredient:
        :param quantity:
        :return:
        """
        x = find_ingredient(ingredient)
        if isinstance(x, IngredientObj):
            # Adding converted ingredient to list
            self.recipe.ingredients_list.append(x)
            self.recipe.quantities[x.name] = quantity
            return True
        else:
            return False

    def remove_ingredient(self, ingredient):

        self.recipe.ingredients_list.remove(ingredient)
        logging.debug("Removed ingredient : " + str(ingredient.name))

    def save_recipe(self):

        FoodThingsGlobal.recipe_list.append(self.recipe)
        self.continue_polling = False

    def change_ingredient_weight(self, index):

        self.display_ingredient_macros(index)

        new_weight = get_int_input("Enter new weight > ", 1, 9999999)
        multiplier = find_weight_multiplier(new_weight, self.recipe.ingredients_list[index])
        self.recipe.ingredients_list[index].convert_portions(multiplier)

        self.display_ingredient_macros(index)

    def display_ingredient_macros(self, index):
        print("Current weight for 1 x {0} is {1}g.\tTotal Carbs : {2}g\tTotal fat : {3}g\tProtein : {4}g"
              .format(self.recipe.ingredients_list[index].name,
                      self.recipe.ingredients_list[index].serving_weight,
                      self.recipe.ingredients_list[index].total_carbs,
                      self.recipe.ingredients_list[index].total_fat,
                      self.recipe.ingredients_list[index].protein))

    def display_recipe_macros(self):
        for name, quantity in self.recipe.quantities.items():
            ingredient = None
            for item in self.recipe.ingredients_list:
                if item.name == name:
                    ingredient = item
                    break
            print("{0} x {1} || Calories: {2}, Carbs: {3}g, Fats: {4}g, Protein: {5}g"
                  .format(str(quantity), str(name),
                          str(float(ingredient.calories) * int(quantity)),
                          str(float(ingredient.total_carbs) * int(quantity)),
                          str(float(ingredient.total_fat) * int(quantity)),
                          str(float(ingredient.protein) * int(quantity))))

        short_macros = self.get_recipe_total_macros_short()
        print("Recipe totals : ")
        print(short_macros)

    def get_recipe_total_macros_short(self):
        return_dict = {"total_cals": 0, "total_fats": 0, "total_carbs": 0, "total_protein": 0}

        for name, quantity in self.recipe.quantities.items():
            ingredient = None
            for item in self.recipe.ingredients_list:
                if item.name == name:
                    ingredient = item
                    break

            return_dict["total_cals"] += float(ingredient.calories) * int(quantity)
            return_dict["total_carbs"] += float(ingredient.total_carbs) * int(quantity)
            return_dict["total_fats"] += float(ingredient.total_fat) * int(quantity)
            return_dict["total_protein"] += float(ingredient.protein) * int(quantity)

        return return_dict

    def return_all_ingredient_names_n_quantities(self):
        return self.recipe.quantities

    def return_all_ingredient_obj(self):
        return self.recipe.ingredients_list


# load_ingredient()
# x = RecipeFuncs()
# x.create_and_edit()
