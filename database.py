import sqlite3
from tabulate import tabulate

#-------------DATABASE SETUP-----------------
# Connect to database (creates file if not exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    marks REAL,
    address TEXT,
    email TEXT UNIQUE
)
""")
conn.commit()