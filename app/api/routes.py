from flask import Blueprint
from app.api.api_utils import (random_device_and_manufacturer, random_ipv4, random_time_in_past_month,
                               random_vulnerability_and_description, random_risk_level)

api_bp = Blueprint("api", __name__)

@api_bp.route("/report")
def gen_report():
    num_of_records = 10
    records = []
    for _ in range(num_of_records):
        device_type, manufacturer = random_device_and_manufacturer()
        vulnerability, vulnerability_desc = random_vulnerability_and_description()
        record = {
            "device_type": device_type,
            "manufacturer": manufacturer,
            "ip": random_ipv4(),
            "date": random_time_in_past_month(),
            "vulnerability": vulnerability,
            "vulnerability_desc": vulnerability_desc,
            "risk_level": random_risk_level()
        }
        records.append(record)
    return records