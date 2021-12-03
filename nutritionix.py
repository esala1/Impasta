"""
This file includes functions that connect to Nutritionix API and retrieve nutrition information
"""
import os
from json.decoder import JSONDecodeError
import requests
from dotenv import load_dotenv

load_dotenv()


def get_nutrition_values(food):
    """
    This function accepts food as its input and uses it to make a get request to
    nutritionix api and retrieve nutrition information.
    """
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
        j_response = response.json()
    except JSONDecodeError:
        return error

    try:
        if "error_message" in j_response:
            return error
        nf_calories, nf_total_fat, nf_serving_size_qty = extract_nutrition_values(
            j_response
        )
        if nf_calories is None or nf_total_fat is None or nf_serving_size_qty is None:
            return error
        return (
            "Calories: "
            + str(nf_calories)
            + ", Total Fat: "
            + str(nf_total_fat)
            + ", Serving Size: "
            + str(nf_serving_size_qty)
        )
    except IndexError:
        return error
    except KeyError:
        return error


def extract_nutrition_values(j_response):
    """
    This function accepts the json response from the get request as input and parses
    the json to retrieve desired values (i.e, nf_calories, nf_total_fat, nf_serving_size_qty).
    """
    try:
        nf_calories = j_response["hits"][0]["fields"]["nf_calories"]
        nf_total_fat = j_response["hits"][0]["fields"]["nf_total_fat"]
        nf_serving_size_qty = j_response["hits"][0]["fields"]["nf_serving_size_qty"]
        return nf_calories, nf_total_fat, nf_serving_size_qty
    except KeyError:
        return None, None, None
    except IndexError:
        return None, None, None
