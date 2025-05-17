from weather_data import collect_data
from analysis import compute_stats
import time

def main():
    data_log = []

    print("Collecting 5 samples...")
    for _ in range(5):
        reading = collect_data()
        print(f"Collected: {reading}")
        data_log.append(reading)
        time.sleep(1)

    print("\nTemperature Stats:", compute_stats(data_log, "temperature"))
    print("Humidity Stats:", compute_stats(data_log, "humidity"))

if __name__ == "__main__":
    main()