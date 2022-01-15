import numpy as np
import os
import requests
# import HTMLSession from requests_html
from requests_html import HTMLSession
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from application.FoodThingsGlobal import FoodThingsGlobal
import pandas as pd
from selenium.webdriver.chrome.options import Options

os.chdir("./dataset")

with np.load('simplified-recipes-1M.npz') as data:

    FoodThingsGlobal.ingredients = data['ingredients']
    # for item in FoodThingsGlobal.ingredients:
    #     print(item)

# os.chdir("../chromedriver")
#
# options = Options()
# options.headless = True
# driver = webdriver.Chrome("chromedriver.exe", options=options )
#
# my_list = []
#
# counter = 0
#
# for item in FoodThingsGlobal.ingredients:
#     counter += 1
#     print("Current item : " + str(item) + " : " + str(counter))
#
#
#     website = "https://www.nutritionix.com/food/" + str(item)
#
#     my_dict = {}
#
#     driver.get(website)
#     timeout = 5
#     try :
#         WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "label-container")))
#     except Exception as e:
#         print("Website not working " + website)
#         print(str(counter))
#         continue
#
#     if WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "label-container"))):
#         x = driver.find_element(By.CLASS_NAME, 'label-container').text
#
#         y = x.split("\n")
#         my_dict["Name"] = y[1]
#         servings = None
#         if "(" in str(y[3]):
#             servings = y[3].split("(")
#         elif "(" in str(y[2]):
#             servings = y[2].split("(")
#
#         my_dict["serving weight"] = servings[1]
#         my_dict["serving size"] = servings[0]
#
#         counter2 = 0
#         for line in y:
#             if line.lower().startswith("calories"):
#                 try:
#                     my_dict["calories"] = line.split(" ")[1]
#                 except Exception as e:
#                     my_dict["calories"] = y[counter2 + 1]
#             if line.lower().startswith("total fat "):
#                 my_dict["total fat"] = line.split(" ")[2]
#             if line.lower().startswith("saturated fat "):
#                 my_dict["saturated fat"] = line.split(" ")[2]
#             if line.lower().startswith("trans fat "):
#                 my_dict["trans fat"] = line.split(" ")[2]
#             if line.lower().startswith("polyunsaturated fat "):
#                 my_dict["polyunsaturated fat"] = line.split(" ")[2]
#             if line.lower().startswith("monounsaturated fat "):
#                 my_dict["monounsatured fat"] = line.split(" ")[2]
#             if line.lower().startswith("cholesterol "):
#                 my_dict["cholesterol"] = line.split(" ")[1]
#             if line.lower().startswith("sodium "):
#                 my_dict["sodium"] = line.split(" ")[1]
#             if line.lower().startswith("potassium "):
#                 my_dict["potassium"] = line.split(" ")[1]
#             if line.lower().startswith("total carbohydrates "):
#                 my_dict["total carbohydrates"] = line.split(" ")[2]
#             if line.lower().startswith("dietary fiber "):
#                 my_dict["dietary fiber"] = line.split(" ")[2]
#             if line.lower().startswith("sugars "):
#                 my_dict["sugars"] = line.split(" ")[1]
#             if line.lower().startswith("protein "):
#
#                 my_dict["protein"] = line.split(" ")[1]
#             counter2 += 1
#
#         my_list.append(my_dict)
#
# df = pd.DataFrame(my_list)
#
# df.to_pickle("ingredients_df.pkl")  # where to save it, usually as a .pkl