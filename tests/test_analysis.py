from analysis import compute_stats

def test_compute_stats_temperature():
    data = [
        {"temperature": 20.0}, {"temperature": 25.0}, {"temperature": 30.0}
    ]
    stats = compute_stats(data, "temperature")
    assert stats["min"] == 20.0
    assert stats["max"] == 30.0
    assert stats["average"] == 25.0

def test_compute_stats_humidity():
    data = [
        {"humidity": 40.0}, {"humidity": 60.0}, {"humidity": 80.0}
    ]
    stats = compute_stats(data, "humidity")
    assert stats["min"] == 40.0
    assert stats["max"] == 80.0
    assert stats["average"] == 60.0