import streamlit as st
import subprocess

st.title("Admin Dashboard")

menu = [
    "Analytics",
    "User Management",
    "Reports",
    "Start Attendance"
]

choice = st.sidebar.selectbox("Admin Menu", menu)

if choice == "Analytics":
    exec(open("admin/analytics.py").read())

elif choice == "User Management":
    exec(open("admin/users.py").read())

elif choice == "Reports":
    exec(open("admin/reports.py").read())

elif choice == "Start Attendance":
    st.warning("Press ESC to stop camera")

    if st.button("Start Camera"):
        subprocess.run(["python", "recognition/recognize.py"])