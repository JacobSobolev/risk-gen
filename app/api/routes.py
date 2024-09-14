from flask import Blueprint
from app.api.api_utils import (random_device_and_manufacturer, random_ipv4, random_time_in_past_month,
                               random_vulnerability_and_description)

api_bp = Blueprint("api", __name__)

import random

def generate_random_ipv4():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

@api_bp.route("/report")
def gen_report():
    device_type, manufacturer = random_device_and_manufacturer()
    vulnerability, vulnerability_desc = random_vulnerability_and_description()
    record = {
        "device_type": device_type,
        "manufacturer": manufacturer,
        "ip": random_ipv4(),
        "date": random_time_in_past_month(),
        "vulnerability": vulnerability,
        "vulnerability_desc": vulnerability_desc
    }
    return record