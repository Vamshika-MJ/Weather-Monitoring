import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
def get_db_connection():
    conn = sqlite3.connect('weather.db')
    return conn

# Set up the database schema (run once)
def setup_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create table to store daily weather summaries
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            city TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            condition TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Run database setup
if __name__ == "__main__":
    setup_db()
    print("Database setup complete.")
