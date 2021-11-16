import requests
import os
from dotenv import load_dotenv

load_dotenv()

#This endpoint enables users to search for restaurants with the purpose of returning the selected restaurant's id for endpoint2: 
# Users have filters like zipcode, address, etc..
# parse through to get restaurant id
def endpoint1():

    #users search by the following parameters, which will be inputted from html form inputs:
    restaurant_name = "Hard Rock Cafe"
    state = "Georgia"
    zip_code = "30308"
    address = "International Boulevard Northeast"
    select_number_of_results = "10"
    
    url = "https://documenu.p.rapidapi.com/restaurants/search/fields"
    querystring = {"restaurant_name":restaurant_name, "address": address,"state":state,"zip_code":zip_code, "size":select_number_of_results}

    headers = {
        'x-api-key': os.getenv('x-api-key'),
        'x-rapidapi-host': os.getenv("x-rapidapi-host-documenu"),
        'x-rapidapi-key': os.getenv('x-rapidapi-key')
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    Jresponse = response.json()
    restaurant_id_parsed = Jresponse['data'][0]['restaurant_id']
    return restaurant_id_parsed
    

restaurant_id = endpoint1()


#this endpoint gets menu information about ONE restaurant 
def endpoint2(restaurant_id):
    #using restaurant id from endpoint1, we typecast the int to str concatnate and call this endpoint 
    x = str(restaurant_id)  
    url = "https://documenu.p.rapidapi.com/restaurant/" + x

    headers = {
        'x-api-key': os.getenv('x-api-key'),
        'x-rapidapi-host': os.getenv('x-rapidapi-host-documenu'),
        'x-rapidapi-key': os.getenv('x-rapidapi-key')
        }
    response = requests.request("GET", url, headers=headers)
    Jresponse = response.json()
    #print(Jresponse)

    """
    We can return by the following menu sections with respective prices:
    #appetizers
    #flat bread, etc..
    note: Not every restaurant will have all sections.
    In case some of the parsed sections don't contain any values, our api will break due to index out of bound error.
    So, I implemented try except blocks.
    """
    try:
        #the item names and their prices are under the same dictionary and one can't be available without the other, so either both exist or both not exist
        item_a = Jresponse['result']['menus'][0]['menu_sections'][0]['menu_items'][0]['name']
        item_a_pricing = Jresponse['result']['menus'][0]['menu_sections'][0]['menu_items'][0]['pricing'][0]['priceString']
        print(item_a)
        print(item_a_pricing)
    except IndexError:
        print(end= ' ') #here im not displaying new line

    try:
        item_b = Jresponse['result']['menus'][0]['menu_sections'][1]['menu_items'][0]['name']
        item_b_pricing = Jresponse['result']['menus'][0]['menu_sections'][1]['menu_items'][0]['pricing'][0]['priceString']
        print(item_b)
        print(item_b_pricing)
    except IndexError:
        print(end= ' ')
    
    try:
        item_c = Jresponse['result']['menus'][0]['menu_sections'][2]['menu_items'][0]['name']
        item_c_pricing = Jresponse['result']['menus'][0]['menu_sections'][2]['menu_items'][0]['pricing'][0]['priceString']
        print(item_c)
        print(item_c_pricing)
    except:
        print(end= ' ')
    
    try: 
        item_d = Jresponse['result']['menus'][0]['menu_sections'][3]['menu_items'][0]['name']
        item_d_pricing = Jresponse['result']['menus'][0]['menu_sections'][3]['menu_items'][0]['pricing'][0]['priceString']
        print(item_d)
        print(item_d_pricing)
    except:
        print(end= ' ')
    
    try:
        item_e = Jresponse['result']['menus'][0]['menu_sections'][4]['menu_items'][0]['name']
        item_e_pricing = Jresponse['result']['menus'][0]['menu_sections'][4]['menu_items'][0]['pricing'][0]['priceString']
        print(item_e)
        print(item_e_pricing)
    except:
        print(end= ' ')

    try:
        item_f = Jresponse['result']['menus'][0]['menu_sections'][5]['menu_items'][0]['name']
        item_f_pricing = Jresponse['result']['menus'][0]['menu_sections'][5]['menu_items'][0]['pricing'][0]['priceString']
        print(item_f)
        print(item_f_pricing)
    except:
        print(end= ' ')
        

endpoint2(restaurant_id)