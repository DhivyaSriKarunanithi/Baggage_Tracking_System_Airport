import sqlite3
from datetime import datetime
import os

class Database:
    def __init__(self):
        self.db_path = os.path.join(os.getcwd(), 'baggage_tracking.db')
        self.conn = sqlite3.connect(self.db_path)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS baggage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    passenger_name TEXT,
                    flight_number TEXT,
                    baggage_id TEXT UNIQUE,
                    status TEXT,
                    last_updated TIMESTAMP
                )
            """)

    def register_baggage(self, passenger_name, flight_number, baggage_id):
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO baggage (passenger_name, flight_number, baggage_id, status, last_updated)
                    VALUES (?, ?, ?, 'Registered', ?)
                """, (passenger_name, flight_number, baggage_id, datetime.now()))
        except sqlite3.IntegrityError:
            print(f"Baggage ID {baggage_id} is already registered.")

    def update_baggage_status(self, baggage_id, status):
        with self.conn:
            self.conn.execute("""
                UPDATE baggage
                SET status = ?, last_updated = ?
                WHERE baggage_id = ?
            """, (status, datetime.now(), baggage_id))

    def get_baggage_info(self, baggage_id):
        with self.conn:
            cur = self.conn.execute("""
                SELECT * FROM baggage
                WHERE baggage_id = ?
            """, (baggage_id,))
            return cur.fetchone()

    def close(self):
        self.conn.close()
