from app.services.elastic_service import ElasticService
from app.services.data_service import (
    get_order,
    get_customer,
    get_product,
)


class SearchService:

    def __init__(self):

        self.elastic = ElasticService()

        self.elastic.connect()

    def knowledge_source(self):

        return {
            "provider": "JSON",
            "mode": "Local Knowledge Base",
            "future_provider": "Elasticsearch Hybrid Search"
        }

    def get_order(self, order_id):

        order = self.elastic.search_order(order_id)

        if order:
            return order

        return get_order(order_id)

    def get_customer(self, customer_id):

        customer = self.elastic.search_customer(customer_id)

        if customer:
            return customer

        return get_customer(customer_id)

    def get_product(self, product_id):

        product = self.elastic.search_product(product_id)

        if product:
            return product

        return get_product(product_id)