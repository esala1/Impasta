from json.decoder import JSONDecodeError
import requests
import os
from dotenv import load_dotenv
from nutritionix import get_nutrition_values

load_dotenv()

# This endpoint enables users to search for restaurants with the purpose of returning the selected restaurant's id for endpoint2:
# Users have filters like zipcode, address, etc..
# parse through to get restaurant id
def get_restaurant_id(restaurant_name, restaurant_address):
    select_number_of_results = "10"

    url = "https://documenu.p.rapidapi.com/restaurants/search/fields"
    querystring = {
        "restaurant_name": restaurant_name,
        "address": restaurant_address,
        "size": select_number_of_results,
    }

    headers = {
        "x-api-key": os.getenv("x-api-key"),
        "x-rapidapi-host": os.getenv("x-rapidapi-host-documenu"),
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        Jresponse = response.json()
    except JSONDecodeError:
        return "Error"

    try:
        restaurant_id_parsed = Jresponse["data"][0]["restaurant_id"]
    except IndexError:
        return "Error"
    return restaurant_id_parsed


# this endpoint gets menu information about ONE restaurant
def get_restaurant_info(restaurant_id):
    # using restaurant id from endpoint1, we typecast the int to str concatnate and call this endpoint
    rid = str(restaurant_id)
    url = f"https://documenu.p.rapidapi.com/restaurant/{rid}"

    headers = {
        "x-api-key": os.getenv("x-api-key"),
        "x-rapidapi-host": os.getenv("x-rapidapi-host-documenu"),
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
    }
    response = requests.request("GET", url, headers=headers)
    Jresponse = response.json()

    """
    We can return by the following menu sections with respective prices:
    #appetizers
    #flat bread, etc..
    note: Not every restaurant will have all sections.
    In case some of the parsed sections don't contain any values, our api will break due to index out of bound error.
    So, I implemented try except blocks.
    """

    menu = []
    description_error = "Description for this item does not exist"

    try:
        menu_options = Jresponse["result"]["menus"][0]["menu_sections"]
        for items in menu_options:
            print(items)
            print("-" * 50)
            menu_items = items["menu_items"][0]
            food_name = menu_items["name"]
            price = menu_items["pricing"][0]["priceString"]
            description = menu_items["description"]
            if description == "":
                description = description_error
            nutrition_values = get_nutrition_values(food_name)
            menu.append(
                {
                    "name": food_name,
                    "price": price,
                    "description": description,
                    "nutrition": nutrition_values,
                }
            )
    except IndexError:
        menu.append(
            {
                "error": "Index Error",
            }
        )

    return menu
