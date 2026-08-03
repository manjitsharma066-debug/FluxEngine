import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_json(filename):
    with open(DATA_DIR / filename, "r") as file:
        return json.load(file)


def get_order(order_id):
    orders = load_json("orders.json")

    for order in orders:
        if order["order_id"] == order_id:
            return order

    return None


def get_customer(customer_id):
    customers = load_json("customers.json")

    for customer in customers:
        if customer["customer_id"] == customer_id:
            return customer

    return None


def get_product(product_id):
    products = load_json("products.json")

    for product in products:
        if product["product_id"] == product_id:
            return product

    return None