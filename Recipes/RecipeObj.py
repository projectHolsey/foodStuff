from Foods.IngredientObj import IngredientObj
from Foods.IngredientFunctions import find_ingredient


class RecipeObj:
    def __init__(self):
        self.name = None
        self.ingredients_list = []
        self.quantities = {}
        self.total_cals = 0



