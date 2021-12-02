"""
This file is the backbone for the Google Maps API.
It detects users' distance when they access this website
based on their IP addresses.
"""
import os
from geocoder.api import ip
import requests
import geocoder
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


def miles_to_meters(miles):
    """
    This method, given miles as its parameter, converts miles to meters.
    Try and except blocks are used to return an error, which is 0.
    """
    return miles * 1_609.344


def place_detail(place_id):
    """
    This function, using place_id as a parameter, return a raw JSON and
    parses specified values(like price_level) into variables for later use.
    Additionally, a dictionary is created to store other parsed data and return it.
    """
    try:
        url = "https://maps.googleapis.com/maps/api/place/details/json?"

        response = requests.get(url + "place_id=" + place_id + "&key=" + API_KEY)

        response_json = response.json()

        if "price_level" in response_json["result"]:
            price_level = response_json["result"]["price_level"]
        else:
            price_level = ""
        res_rating = ""

        if "rating" in response_json["result"]:
            res_rating = response_json["result"]["rating"]

        res_dict = {
            "res_name": response_json["result"]["name"],
            "res_rating": res_rating,
            "res_price_level": price_level,
            "res_user_rating": response_json["result"]["user_ratings_total"]
            if "user_ratings_total" in response_json["result"]
            else "",
            "res_icon": response_json["result"]["icon"],
            "res_photo": place_photo(
                response_json["result"]["photos"][0]["photo_reference"]
            )
            if "photos" in response_json["result"]
            else "",
            "res_address": response_json["result"]["formatted_address"],
            "res_phone_number": response_json["result"]["formatted_phone_number"]
            if "formatted_phone_number" in response_json["result"]
            else "",
        }
    except KeyError:
        return "error"
    except IndexError:
        return "error"

    return res_dict


def place_photo(photo_reference):
    """
    This method uses an endpoint from Google map api containing url links
    for restaurant photos. Then we return the response, the photos.
    """

    url = "https://maps.googleapis.com/maps/api/place/photo?"

    response = (
        url + "maxwidth=200" + "&photo_reference=" + photo_reference + "&key=" + API_KEY
    )

    return response


def nearby_restaurants(ip_address):
    """
    This function calculates nearby restaurants using ip_address as an input.
    Utilizing geocoder, which is a class, it calculates the longtitude and longtitude
    coordinates. A different API endpoint is being used here to return response.
    And that is parsed and the method ultimately returns a list with the nearest
    restaurants near the users
    """
    geo = geocoder.ipinfo(ip_address)
    myloc = str(geo.lat) + "%2C" + str(geo.lng)

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

    response_json = response.json()

    if "next_page_token" in response_json:
        next_page_token = response_json["next_page_token"]
    else:
        next_page_token = ""

    for i in range(len(response_json["results"]) // 5):
        res_list.append(place_detail(response_json["results"][i]["place_id"]))

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

        response_json = response.json()

        for i in range(len(response_json["results"]) // 5):
            res_list.append(place_detail(response_json["results"][i]["place_id"]))

        if "next_page_token" in response_json:
            next_page_token = response_json["next_page_token"]
        else:
            next_page_token = ""
    return res_list
