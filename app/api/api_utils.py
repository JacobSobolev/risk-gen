import random
from datetime import datetime, timedelta
from app.api.data import device_manufacturers, security_vulnerabilities

device_types_list = list(device_manufacturers.keys())
security_vul_list = list(security_vulnerabilities.keys())

def random_ipv4():
    """return a random ip v4"""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def random_time_in_past_month():
    """return a random date for the last month"""
    random_days = random.randint(0, 30)
    random_date = datetime.now() - timedelta(days=random_days)

    random_seconds = random.randint(0, 86400)
    random_time = timedelta(seconds=random_seconds)

    random_datetime = datetime.combine(random_date, datetime.min.time()) + random_time
    return random_datetime


def random_device_and_manufacturer():
    """return a random device type and possible manufacturer"""
    device_type = random.choice(device_types_list)
    manufacturer = random.choice(device_manufacturers[device_type])

    return device_type, manufacturer

def random_vulnerability_and_description():
    vulnerability = random.choice(security_vul_list)
    vulnerability_desc = security_vulnerabilities[vulnerability]

    return vulnerability, vulnerability_desc
