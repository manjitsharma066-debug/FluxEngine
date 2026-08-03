import json

from app.config.settings import POLICIES_FILE
from app.services.search_service import SearchService
from app.services.audit_service import save_audit_log

search = SearchService()


def check_refund(order_id, reason):

    order = search.get_order(order_id)

    if not order:
        return {
            "status": "Rejected",
            "refund_amount": 0,
            "policy": "Order Not Found"
        }

    customer = search.get_customer(order["customer_id"])

    product = search.get_product(order["product_id"])

    with open(POLICIES_FILE, "r") as file:
        policies = json.load(file)

    selected_policy = None

    for policy in policies:

        if policy["reason"] == reason:
            selected_policy = policy
            break

    if selected_policy is None:

        return {
            "status": "Pending",
            "refund_amount": 0,
            "policy": "Manual Review Required"
        }

    response = {
        **selected_policy,
        "customer": customer["name"],
        "product": product["name"],
        "knowledge_source": search.knowledge_source()
    }

    save_audit_log(
        {
            "order_id": order_id,
            "customer": customer["name"],
            "product": product["name"],
            "reason": reason,
            "status": response["status"],
            "refund_amount": response["refund_amount"]
        }
    )

    return response