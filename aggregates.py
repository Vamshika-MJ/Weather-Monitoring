from collections import defaultdict
import sqlite3
from db_setup import get_db_connection

# Store daily data in memory for aggregation
daily_data = defaultdict(list)

def process_weather_data(weather):
    city = weather['city']
    daily_data[city].append(weather['temp'])  # Add temperature to the city's daily list

def calculate_daily_summary():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for city, temps in daily_data.items():
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        dominant_condition = "Clear"  # Placeholder: Add logic to determine dominant condition
        cursor.execute("INSERT INTO daily_summary (city, avg_temp, max_temp, min_temp, condition) VALUES (?, ?, ?, ?, ?)",
                       (city, avg_temp, max_temp, min_temp, dominant_condition))
        conn.commit()

    # Clear the daily data after calculating the summary
    daily_data.clear()

    print("Daily summary calculated and saved to the database.")
