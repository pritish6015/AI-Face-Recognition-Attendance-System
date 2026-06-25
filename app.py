import streamlit as st
import sqlite3
from auth.login import login_page
from auth.auth_utils import hash_password

import database.database
import streamlit.components.v1 as components

if st.sidebar.button("🏠 Main Portal"):

    components.html(
        """
        <script>
            window.open(
                'http://localhost:8502',
                '_self'
            );
        </script>
        """,
        height=0,
    )


st.set_page_config(
    page_title="Enterprise AI Attendance System",
    layout="wide"
)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM users WHERE username='admin'")
admin = cursor.fetchone()

if not admin:
    cursor.execute(
        """
        INSERT INTO users
        (unique_id, full_name, username, password, role, department, created_at)
        VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
        """,
        (
            "ADMIN-001",
            "System Admin",
            "admin",
            hash_password("admin123"),
            "admin",
            "Administration"
        )
    )

    conn.commit()


if not st.session_state.logged_in:
    login_page()

else:
    user = st.session_state.user

    role = user[5]

    st.sidebar.success(f"Logged in as {role}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

    if role == "admin":
        exec(open("admin/dashboard.py").read())

    else:
        exec(open("user/dashboard.py").read())