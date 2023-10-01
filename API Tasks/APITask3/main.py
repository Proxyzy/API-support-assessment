from dataclasses import dataclass
import operator
import requests
import json

auth_key = ""

url_get = "https://lt-support.revelup.com/weborders/menu/?establishment=101"

url_post = "https://lt-support.revelup.com/specialresources/cart/validate/"

get_header = {
    "accept": "application/json"
    }


post_headers = {
    "accept": "application/json",
    "API-AUTHENTICATION": f"{auth_key}"
}

@dataclass
class Product:
    price: float
    id: int

products_array = []

response = requests.get(url_get, headers = get_header)

parse_to_json = json.loads(response.text)

if len(parse_to_json['data']['categories']) > 0:
    products = parse_to_json['data']['categories'][0]['products']
    for product in products:
        products_array.append(Product(product['price'], product['id']))

    products_array = sorted(products_array, key=operator.attrgetter("price"))
else:
    print("No product found")

calculate_products = []

for element in range(3):
    product = {
        "price": products_array[element].price,
        "product": products_array[element].id,
        "quantity": 1
    }
    calculate_products.append(product)

print(calculate_products)

body = {
    "establishment": 1,
    "items": calculate_products,
    "orderInfo":
    {
        "dining_option": 0
    }
}

post_responce = requests.post(url_post, headers=post_headers, json=body)

post_responce = json.loads(post_responce.text)

print(f"Subtotal: {post_responce['data']['subtotal']}")
print(f"Tax: {post_responce['data']['tax']}")
print(f"Final Total: {post_responce['data']['final_total']}")