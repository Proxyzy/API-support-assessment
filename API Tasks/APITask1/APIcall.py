import requests
import json

auth_key = ""

url = "https://lt-support.revelup.com/resources/OrderItem/?fields=&order_by=-created_date"

headers = {
    "accept": "application/json",
    "API-AUTHENTICATION": f"{auth_key}"
}


def get_order_items(offset):
    response = requests.get(url + f"&offset={50*offset}", headers=headers)
    parse_json = json.loads(response.text)
    order_items = parse_json["objects"]
    return order_items

def get_first_eatin_order(offset):
    items = get_order_items(offset)
    if items == []:
        print("No EatIn order found!")
        return
    for item in items:
        if item['dining_option'] == 1:
            order = item['order']
            find_expensive_item(order, items, offset)
            return
    return get_first_eatin_order(offset+1)

def find_expensive_item(order_number, items_list, offset):
    max = -1
    for item in items_list:
        if order_number != item['order'] and max > -1:
            order = str(item['order']).replace('/resources/Order/', '').replace('/', '')
            print(f"Order number: {order}")
            print(f"{item['product_name_override']} - Price {item['price']} - Tax {item['tax_amount']}")
            return
        if item['order'] == order_number and max < item['price']:
            max = item['price']
    items_list = get_order_items(offset+1)
    find_expensive_item(order_number, items_list, offset+1)


get_first_eatin_order(0)





    
