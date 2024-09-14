import random
from datetime import datetime, timedelta
from app.api.data import device_manufacturers

def random_ipv4():
    """return a random ip v4"""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def random_time_in_past_month():
    """return a random date for the last month"""
    now = datetime.now()
    start_date = now - timedelta(days=30)
    delta_days = (now - start_date).days
    random_days = random.randint(0, delta_days)
    random_date = start_date + timedelta(days=random_days)

    random_seconds = random.randint(0, 86399)
    random_time = timedelta(seconds=random_seconds)

    random_datetime = datetime.combine(random_date, datetime.min.time()) + random_time
    return random_datetime


def random_device_and_manufacturer():
    """return a random device type and possible manufacturer"""
    device_type = random.choice(list(device_manufacturers.keys()))
    manufacturer = random.choice(device_manufacturers[device_type])

    return device_type, manufacturer

