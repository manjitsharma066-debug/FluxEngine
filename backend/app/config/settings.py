from pathlib import Path

# Project Paths
BASE_DIR = Path(__file__).parent.parent

DATA_DIR = BASE_DIR / "data"

# Data Files
ORDERS_FILE = DATA_DIR / "orders.json"

CUSTOMERS_FILE = DATA_DIR / "customers.json"

PRODUCTS_FILE = DATA_DIR / "products.json"

POLICIES_FILE = DATA_DIR / "refund_policies.json"

AUDIT_FILE = DATA_DIR / "audit_logs.json"

# Future Elasticsearch
ELASTIC_HOST = "http://localhost:9200"

ELASTIC_INDEX_ORDERS = "orders"

ELASTIC_INDEX_PRODUCTS = "products"

ELASTIC_INDEX_CUSTOMERS = "customers"

ELASTIC_INDEX_POLICIES = "refund_policies"

ELASTIC_INDEX_AUDIT = "audit_logs"