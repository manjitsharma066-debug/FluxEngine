import json

from app.config.settings import (
    ORDERS_FILE,
    CUSTOMERS_FILE,
    PRODUCTS_FILE,
)


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def get_order(order_id):

    orders = load_json(ORDERS_FILE)

    for order in orders:

        if order["order_id"] == order_id:
            return order

    return None


def get_customer(customer_id):

    customers = load_json(CUSTOMERS_FILE)

    for customer in customers:

        if customer["customer_id"] == customer_id:
            return customer

    return None


def get_product(product_id):

    products = load_json(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:
            return product

    return None