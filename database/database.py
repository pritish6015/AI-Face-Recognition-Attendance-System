import sqlite3
from datetime import datetime

DB_NAME = "attendance.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unique_id TEXT UNIQUE,
    full_name TEXT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT,
    department TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unique_id TEXT,
    full_name TEXT,
    date TEXT,
    check_in TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS login_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    login_time TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS system_state (
    id INTEGER PRIMARY KEY,
    current_user TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO system_state(id, current_user)
VALUES(1, NULL)
""")

conn.commit()
conn.close()