from flask import Blueprint, request
from app.api.api_utils import (random_device_and_manufacturer, random_ipv4, random_time_in_past_month,
                               random_vulnerability_and_description, random_risk_level)

DEFUALT_NUM_RECORDS = 10
MAX_NUM_RECORDS = 100

api_bp = Blueprint("api", __name__)

@api_bp.route("/report")
def gen_report():
    try:
        num_records = int(request.args.get('records', default=DEFUALT_NUM_RECORDS))
    except ValueError:
        num_records = DEFUALT_NUM_RECORDS
    if num_records < 0 or num_records > MAX_NUM_RECORDS:
        num_records = DEFUALT_NUM_RECORDS

    records = []
    for _ in range(num_records):
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