import json
from pathlib import Path
from datetime import datetime

LOG_FILE = Path(__file__).parent.parent / "data" / "audit_logs.json"


def save_audit_log(log_data):

    # Create file if missing
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w") as file:
            json.dump([], file)

    # Read existing logs
    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    except json.JSONDecodeError:
        logs = []

    # Add timestamp
    log_data["timestamp"] = datetime.now().isoformat(timespec="seconds")

    logs.append(log_data)

    # Save back
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

    print("✅ Audit Log Saved")