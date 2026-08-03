import json
from pathlib import Path

from app.services.data_service import (
    get_order,
    get_customer,
    get_product,
)

from app.services.audit_service import save_audit_log


DATA_FILE = Path(__file__).parent.parent / "data" / "refund_policies.json"


def check_refund(order_id, reason):

    # Get Order
    order = get_order(order_id)

    if not order:
        return {
            "status": "Rejected",
            "refund_amount": 0,
            "policy": "Order Not Found"
        }

    # Get Customer
    customer = get_customer(order["customer_id"])

    # Get Product
    product = get_product(order["product_id"])

    # Load Refund Policies
    with open(DATA_FILE, "r") as file:
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

    # Prepare Response
    response = {
        **selected_policy,
        "customer": customer["name"],
        "product": product["name"]
    }

    # Save Audit Log
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