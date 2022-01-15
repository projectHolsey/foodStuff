import numpy as np
import os

from Foods.IngredientObj import IngredientObj
from application.FoodThingsGlobal import FoodThingsGlobal
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))


def load_ingredient():

    os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/dataset")

    FoodThingsGlobal.dataset = pd.read_pickle("ingredients_df.pkl")

    # print(list(FoodThingsGlobal.dataset))

    os.chdir(dir_path)

    create_ingredients_obj_list()


def create_ingredients_obj_list():
    counter = 0
    for index, item in FoodThingsGlobal.dataset.iterrows():

        ingredient = IngredientObj()

        # Sorting the outliers
        for key, value in item.items():
            if "oz" in str(value):
                if "fl" in str(value):
                    # Skip fluid ounces
                    continue
                if "serving weight" in key:
                    if "/" in value:
                        # Outlier : "3/4 oz" WHY?!!?
                        original_val = value
                        splits = str(value).split(" ")
                        splits = splits[0].split("/")
                        splits = float(splits[0]) / float(splits[1])
                        value = splits
                        if "of" in original_val:
                            # outliner : "1/12 of 12 oz cake)"
                            splits = str(original_val).split(" ")
                            splits = splits[2]
                            value = (float(value) * float(splits))
                    value = str(value).strip()
                    new_val = str(value).split(" ")
                    new_val = new_val[0]
                    new_val = float(new_val) * 28.3495
                    item[key] = new_val
            if str(value).endswith("mg"):
                # print(value)
                new_val = value.replace("mg", "")
                new_val = float(new_val) / 1000
                item[key] = new_val

        ingredient.name = item["Name"]
        if "Serving" in ingredient.name:
            continue
        ingredient.serving_weight = str(item["serving weight"]).replace("g", "")
        ingredient.serving = item["serving size"]
        ingredient.calories = item["calories"]
        ingredient.total_fat = str(item["total fat"]).replace("g", "")
        ingredient.saturated_fat = str(item["saturated fat"]).replace("g", "")
        ingredient.trans_fat = str(item["trans fat"]).replace("g", "")
        ingredient.polyunsaturated_fat = str(item["polyunsaturated fat"]).replace("g", "")
        ingredient.monounsaturated_fat = str(item["monounsatured fat"]).replace("g", "")
        ingredient.cholesterol = str(item["cholesterol"]).replace("g", "")
        ingredient.sodium = str(item["sodium"]).replace("g", "")
        ingredient.potassium = str(item["potassium"]).replace("g", "")
        ingredient.total_carbs = str(item["total carbohydrates"]).replace("g", "")
        ingredient.dietary_fibre = str(item["dietary fiber"]).replace("g", "")
        ingredient.sugars = str(item["sugars"]).replace("g", "")
        ingredient.protein = str(item["protein"]).replace("g", "")
        ingredient.Id = counter
        counter += 1
        FoodThingsGlobal.ingredients.append(ingredient)


load_ingredient()