import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = "your_actual_api_key"
if not API_KEY:
    raise Exception("API key not found. Ensure it's set correctly in the .env file.")

print(f"Loaded API Key: {API_KEY}")  # Debugging print to confirm the key is loaded

def get_weather_data(city):
    print(f"Fetching weather data for {city}...")  # Debugging line
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    print(f"Response received: {response.status_code}")  # Debugging line
    data = response.json()
    
    if response.status_code != 200 or 'weather' not in data:
        raise Exception(f"Error fetching weather data for {city}: {data.get('message', 'Unknown error')}")
    
    print(f"Parsed weather data: {data}")  # Debugging line
    return {
        'city': city,
        'main': data['weather'][0]['main'],
        'temp': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'timestamp': data['dt']
    }
