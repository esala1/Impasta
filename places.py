from types import resolve_bases
import requests, json
import geocoder
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0


# def get_address(latitude, longitude):
#     geolocator = Nominatim(user_agent="geoapiExercises")
#     location = geolocator.reverse((latitude, longitude))
#     address = location.raw["address"]
#     if "house_number" in address:
#         house_num = address["house_number"]
#     else:
#         house_num = ""

#     return str(
#         house_num
#         + " "
#         + address["road"]
#         + ", "
#         + address["city"]
#         + ", "
#         + address["state"]
#         + " "
#         + address["postcode"]
#         + ", "
#         + address["country"]
#     )


def place_detail(place_id):

    url = "https://maps.googleapis.com/maps/api/place/details/json?"

    response = requests.get(url + "place_id=" + place_id + "&key=" + API_KEY)

    x = response.json()

    if "price_level" in x["result"]:
        price_level = x["result"]["price_level"]
    else:
        price_level = ""

    res_dict = {
        "res_name": x["result"]["name"],
        "res_rating": x["result"]["rating"] if "rating" in x["result"] else "",
        "res_price_level": price_level,
        "res_user_rating": x["result"]["user_ratings_total"]
        if "user_ratings_total" in x["result"]
        else "",
        "res_icon": x["result"]["icon"],
        "res_photo": place_photo(x["result"]["photos"][0]["photo_reference"])
        if "photos" in x["result"]
        else "",
        # "res_address": get_address(
        #     x["result"]["geometry"]["location"]["lat"],
        #     x["result"]["geometry"]["location"]["lng"],
        # ),
        "res_address": x["result"]["formatted_address"],
        "res_phone_number": x["result"]["formatted_phone_number"]
        if "formatted_phone_number" in x["result"]
        else "",
    }

    return res_dict


def place_photo(photo_reference):

    url = "https://maps.googleapis.com/maps/api/place/photo?"

    response = (
        url + "maxwidth=200" + "&photo_reference=" + photo_reference + "&key=" + API_KEY
    )

    return response


def nearby_restaurants():

    g = geocoder.ip("me")
    myloc = str(g.lat) + "%2C" + str(g.lng)

    res_list = []

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    response = requests.get(
        url
        + "location="
        + myloc
        + "&radius="
        + str(miles_to_meters(3))
        + "&type=restaurant|food"
        + "&key="
        + API_KEY
    )

    x = response.json()

    next_page_token = x["next_page_token"]

    for i in range(len(x["results"])):
        res_list.append(place_detail(x["results"][i]["place_id"]))

    while next_page_token:
        response = requests.get(
            url
            + "location="
            + myloc
            + "&radius="
            + str(miles_to_meters(3))
            + "&type=restaurant|food"
            + "&pagetoken="
            + next_page_token
            + "&key="
            + API_KEY
        )

        x = response.json()

        for i in range(len(x["results"])):
            res_list.append(place_detail(x["results"][i]["place_id"]))

        if "next_page_token" in x:
            next_page_token = x["next_page_token"]
        else:
            next_page_token = ""

    return res_list
