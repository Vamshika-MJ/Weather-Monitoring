import schedule
import time
from weather_api import get_weather_data
from aggregates import process_weather_data, calculate_daily_summary
from alerts import check_alerts

# Configurable list of cities
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def fetch_weather():
    print("Fetching weather data...")  # Debugging print
    for city in CITIES:
        weather = get_weather_data(city)
        print(f"Weather data for {city}: {weather}")  # Debugging print
        process_weather_data(weather)  # Process and store the weather data
        check_alerts(weather)  # Check for alerts

# Schedule weather data retrieval every 5 minutes
schedule.every(5).seconds.do(fetch_weather)

# Schedule daily summary calculation at the end of each day
schedule.every().day.at("23:59").do(calculate_daily_summary)

if __name__ == "__main__":
    try:
        print("Starting the weather monitoring system...")  # Debugging print
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
