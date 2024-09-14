from flask import Blueprint
from app.api.api_utils import random_device_and_manufacturer, random_ipv4, random_time_in_past_month

api_bp = Blueprint("api", __name__)

import random

def generate_random_ipv4():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

@api_bp.route("/report")
def gen_report():
    device, manufactorer = random_device_and_manufacturer()
    record = {
        "device": device,
        "manufactorer": manufactorer,
        "ip": random_ipv4(),
        "date": random_time_in_past_month()
    }
    return record