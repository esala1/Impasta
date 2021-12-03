import requests, json
import os
from places import place_detail, place_photo, miles_to_meters

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


def searchRestaurant(search_input):

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

    x = response.json()

    for i in range(len(x["results"]) // 5 + 1):
        res_list.append(place_detail(x["results"][i]["place_id"]))

    print(res_list)

    return res_list


searchRestaurant("9292")
