import random

def get_temperature():
    return round(random.uniform(15.0, 35.0), 2)

def get_humidity():
    return round(random.uniform(30.0, 90.0), 2)

def collect_data():
    return {
        "temperature": get_temperature(),
        "humidity": get_humidity()
    }