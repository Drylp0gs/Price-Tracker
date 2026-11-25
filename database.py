import sqlite3
from datetime import datetime
import pandas as pd

DB_NAME = "prices.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    """Creates the products table if it does not exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            availability TEXT,
            url TEXT,
            scraped_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_items(items):
    """Inserts a list of scraped product dictionaries into SQLite."""
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in items:
        cursor.execute("""
            INSERT INTO price_history (title, price, availability, url, scraped_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            item["title"],
            item["price"],
            item["availability"],
            item["url"],
            timestamp
        ))

    conn.commit()
    conn.close()
    print(f"[DB] Saved {len(items)} records at {timestamp}")

def fetch_all_data():
    """Returns all price records as a Pandas DataFrame."""
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM price_history ORDER BY scraped_at DESC", conn)
    conn.close()
    return df

def export_to_csv(filename="price_report.csv"):
    """Exports the SQLite table to a clean CSV file."""
    df = fetch_all_data()
    df.to_csv(filename, index=False)
    print(f"[EXPORT] Data exported to {filename}")