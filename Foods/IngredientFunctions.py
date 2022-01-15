from application.FoodThingsGlobal import FoodThingsGlobal

import logging


def find_ingredient(ingredient):
    """ If food name is exact, return obj else return None """
    for item in FoodThingsGlobal.ingredients:
        if str(item.name).lower() == str(ingredient).lower():
            logging.debug("Found exact ingredient match!")
            return item
    return None


def find_potential_ingredients(ingredient):
    potentials = []
    for item in FoodThingsGlobal.ingredients:
        if ingredient in item.name:
            potentials.append(item)
            logging.debug("Found potential ingredient")
    return potentials


def find_weight_multiplier(weight, ingredient):
    """
    Converts an ingredients macronutrients based on weight supplied

    :param weight: Weight in grams
    :param ingredient: Ingredient Object
    :return: multiplier
    """

    multiplier = float(weight) / float(ingredient.serving_weight)

    return multiplier




