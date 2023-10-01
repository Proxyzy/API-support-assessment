from dataclasses import dataclass
import operator
import requests
import json

url = "https://lt-support.revelup.com/weborders/menu/?establishment=101"

headers = {
    "accept": "application/json"
}

@dataclass
class Product:
    name: str
    price: float

response = requests.get(url, headers = headers)

parse_to_json = json.loads(response.text)

if len(parse_to_json['data']['categories']) > 0:
    products = parse_to_json['data']['categories'][0]['products']
    products_array = []
    for product in products:
        products_array.append(Product(product['name'], product['price']))

    products_array = sorted(products_array, key=operator.attrgetter("price"))

    for product in products_array:
        print(f"{product.name} - {product.price}")
else:
    print("No product found")



