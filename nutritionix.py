import json
from json.decoder import JSONDecodeError
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# let's use "food" variable to store what users search and return results


def get_nutrition_values(food):
    url = f"https://nutritionix-api.p.rapidapi.com/v1_1/search/%20{food}"

    querystring = {"fields": "item_name,item_id,brand_name,nf_calories,nf_total_fat"}

    # Using RapidAPI, third party api for interfacing, I can access this api and Zomato api

    headers = {
        "x-rapidapi-host": os.getenv("x-rapidapi-host"),
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
    }

    error = "Nutrition information for this item is currently not available"

    try:
        response = requests.get(url, headers=headers, params=querystring)
        Jresponse = response.json()
    except JSONDecodeError:
        return error

    try:
        if "error_message" in Jresponse:
            return error
        nf_calories, nf_total_fat, nf_serving_size_qty = extract_nutrition_values(
            Jresponse
        )
        if nf_calories == None or nf_total_fat == None or nf_serving_size_qty == None:
            return error
        return f"Calories: {nf_calories}, Total Fat: {nf_total_fat}, Serving Size: {nf_serving_size_qty}"
    except IndexError:
        return error
    except KeyError:
        return error


def extract_nutrition_values(Jresponse):
    try:
        nf_calories = Jresponse["hits"][0]["fields"]["nf_calories"]
        nf_total_fat = Jresponse["hits"][0]["fields"]["nf_total_fat"]
        nf_serving_size_qty = Jresponse["hits"][0]["fields"]["nf_serving_size_qty"]
        return nf_calories, nf_total_fat, nf_serving_size_qty
    except KeyError:
        return None, None, None
    except IndexError:
        return None, None, None
