"""
This file is a back-end for Google Text Search API
It will return restaurants information based on user's
input such as location or/and restaurants names
"""
import os
import requests
from places import place_detail, miles_to_meters

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


def search_restaurant(search_input):
    """
    this function takes user's search input as a parameter and pass that value into
    Text Search API end-point to return the ids of restaurants and then pass that id
    into function place_detail which is called from places.py to return restaurants
    data
    """

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    res_list = []

    response = requests.get(
        url
        + "query="
        + search_input
        + "&radius="
        + str(miles_to_meters(1))
        + "&type=restaurant|food"
        + "&key="
        + API_KEY
    )

    json_response = response.json()

    for i in range(len(json_response["results"]) // 5 + 1):
        res_list.append(place_detail(json_response["results"][i]["place_id"]))

    return res_list
