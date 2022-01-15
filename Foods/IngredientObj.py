class IngredientObj:
    def __init__(self):

        self.Id = None
        self.name = None
        self.serving_weight = None
        self.serving = None
        self.calories = None
        self.total_fat = None
        self.saturated_fat = None
        self.trans_fat = None
        self.polyunsaturated_fat = None
        self.monounsaturated_fat = None
        self.cholesterol = None
        self.sodium = None
        self.potassium = None
        self.total_carbs = None
        self.dietary_fibre = None
        self.sugars = None
        self.protein = None

    def convert_portions(self, multiplier):
        """
        Convert this ingredient object to contain multiplier edited macronutrients

        :param multiplier: multiplier for each item
        :return: N/A
        """

        if "fl" in self.serving_weight:
            self.serving_weight = self.serving_weight.split(" ")
            self.serving_weight = float(self.serving_weight[0]) * multiplier
        else:
            self.serving_weight = float(self.serving_weight) * multiplier
        self.calories = float(self.calories) * multiplier
        self.total_fat = float(self.total_fat) * multiplier
        self.saturated_fat = float(self.saturated_fat) * multiplier
        self.trans_fat = float(self.trans_fat) * multiplier
        self.polyunsaturated_fat = float(self.polyunsaturated_fat) * multiplier
        self.monounsaturated_fat = float(self.monounsaturated_fat) * multiplier
        self.cholesterol = float(self.cholesterol) * multiplier
        self.sodium = float(self.sodium) * multiplier
        self.potassium = float(self.potassium) * multiplier
        self.total_carbs = float(self.total_carbs) * multiplier
        self.dietary_fibre = float(self.dietary_fibre) * multiplier
        self.sugars = float(self.sugars) * multiplier
        self.protein = float(self.protein) * multiplier


# ['Name',
# 'serving weight',
# 'serving size',
# 'calories',
# 'total fat',
# 'saturated fat',
# 'trans fat',
# 'polyunsaturated fat',
# 'monounsatured fat',
# 'cholesterol',
# 'sodium',
# 'potassium',
# 'total carbohydrates',
# 'dietary fiber',
# 'sugars',
# 'protein']
