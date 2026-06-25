import bcrypt
import sqlite3
from datetime import datetime

DB_NAME = "attendance.db"


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    if user:
        stored_password = user[4]

        if verify_password(password, stored_password):
            cursor.execute(
                "INSERT INTO login_logs(username, login_time) VALUES (?, ?)",
                (username, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )
            conn.commit()
            conn.close()
            return user

    conn.close()
    return None