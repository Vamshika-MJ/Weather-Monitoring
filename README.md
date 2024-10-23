# Real-Time Weather Monitoring System

## Overview
This project fetches real-time weather data from the OpenWeatherMap API for multiple cities, processes it to generate daily summaries (average, max, min temperatures), and triggers alerts if certain thresholds are breached.

### Features:
- Fetch weather data every 5 minutes.
- Calculate daily rollups (avg, max, min temperatures).
- Trigger alerts if the temperature exceeds 35°C.
- Store daily summaries in SQLite database.

## Setup Instructions

### Requirements:
- Python 3.9+
- SQLite

### Steps:
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
