from application.FoodThingsGlobal import FoodThingsGlobal
from OnStart.LoadIngredients import load_ingredient

import timeit
import time
from timeit import default_timer as timer


def get_ingredient_from_list():
    for item in FoodThingsGlobal.ingredients:
        if str(item.name).lower() == "lemon":
            return item


def get_ingredient_from_df():
    try:
        return FoodThingsGlobal.dataset[str(FoodThingsGlobal.dataset["Name"]).lower() == str("lemon").lower()]
    except Exception as e:
        return None


start = timer()
load_ingredient()
end = timer()
print(end - start)

start = timer()
for x in range(100):
    get_ingredient_from_list()
end = timer()
print(end - start)

start = timer()
for x in range(100):
    get_ingredient_from_df()
end = timer()
print(end - start)

print(timeit.repeat("get_ingredient_from_list()", "from __main__ import get_ingredient_from_list", number=100))
print(timeit.repeat("get_ingredient_from_df()", "from __main__ import get_ingredient_from_df", number=100))
# print(timeit.timeit("get_ingredient_from_list()", "from __main__ import get_ingredient_from_list"))
