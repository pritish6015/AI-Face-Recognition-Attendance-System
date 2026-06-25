import streamlit as st
import sqlite3
import subprocess
from auth.auth_utils import hash_password
import shutil
import os


conn = sqlite3.connect("attendance.db", check_same_thread=False)
cursor = conn.cursor()

st.subheader("User Management")


# =========================
# DEFAULT DEPARTMENTS
# =========================
departments = [
    "BCA",
    "MCA",
    "BBA",
    "MBA",
    "CSE",
    "ECE",
    "ME",
    "CE"
]


# =========================
# AUTO GENERATE UNIQUE ID
# =========================
def generate_unique_id(department, session_year):

    prefix = f"{department}-{session_year}-STU-"

    cursor.execute(
        """
        SELECT unique_id FROM users
        WHERE unique_id LIKE ?
        ORDER BY id DESC LIMIT 1
        """,
        (prefix + "%",)
    )

    last_record = cursor.fetchone()

    if last_record:

        last_id = last_record[0]

        last_number = int(last_id.split("-")[-1])

        new_number = last_number + 1

    else:
        new_number = 1

    return f"{prefix}{new_number:03d}"


# =========================
# ADD NEW USER
# =========================
with st.expander("Add New User"):

    full_name = st.text_input("Full Name")

    department = st.selectbox(
        "Department",
        departments
    )

    session_year = st.selectbox(
        "Session Year",
        [
            "2022",
            "2023",
            "2024",
            "2025",
            "2026"
        ]
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        ["user"]
    )

    # Generate Preview ID
    generated_id = generate_unique_id(
        department,
        session_year
    )

    st.info(f"Generated Unique ID: {generated_id}")

    if st.button("Create User"):

        hashed_password = hash_password(password)

        cursor.execute(
            """
            INSERT INTO users
            (
                unique_id,
                full_name,
                username,
                password,
                role,
                department,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
            """,
            (
                generated_id,
                full_name,
                username,
                hashed_password,
                role,
                department,
            )
        )

        conn.commit()

        # Capture Face Dataset
        subprocess.run(
            ["python", "recognition/add_face.py", generated_id]
        )

        # Train Model
        subprocess.run(
            ["python", "recognition/train_model.py"]
        )

        st.success(
            f"User Created Successfully\n\nUnique ID: {generated_id}"
        )


# =========================
# SHOW ALL USERS
# =========================
st.subheader("All Users")

users = cursor.execute(
    """
    SELECT
        unique_id,
        full_name,
        username,
        role,
        department
    FROM users
    """
).fetchall()

st.table(users)


# =========================
# DELETE USER
# =========================
st.subheader("Delete User")

user_id = st.text_input(
    "Enter Unique ID"
)

if st.button("Delete User"):

    cursor.execute(
        """
        DELETE FROM users
        WHERE unique_id=?
        """,
        (user_id,)
    )

    conn.commit()

    path = f"dataset/{user_id}"

    if os.path.exists(path):
        shutil.rmtree(path)

    subprocess.run(
        ["python", "recognition/train_model.py"]
    )

    st.success("User Deleted Successfully")