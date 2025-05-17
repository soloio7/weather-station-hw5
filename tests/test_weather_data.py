from weather_data import get_temperature, get_humidity

def test_temperature_range():
    for _ in range(10):
        temp = get_temperature()
        assert 15.0 <= temp <= 35.0

def test_humidity_range():
    for _ in range(10):
        humidity = get_humidity()
        assert 30.0 <= humidity <= 90.0