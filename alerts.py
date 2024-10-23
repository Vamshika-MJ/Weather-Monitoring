# Alert when the temperature exceeds the threshold (e.g., 35°C)
ALERT_THRESHOLD = 35

def check_alerts(weather):
    city = weather['city']
    temp = weather['temp']
    
    if temp > ALERT_THRESHOLD:
        print(f"ALERT: Temperature in {city} has exceeded {ALERT_THRESHOLD}°C.")
