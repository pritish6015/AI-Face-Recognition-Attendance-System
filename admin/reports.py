import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("attendance.db")

st.subheader("Attendance Reports")

filter_type = st.selectbox(
    "Filter",
    ["All", "Today", "Monthly", "Yearly"]
)

query = "SELECT * FROM attendance"

if filter_type == "Today":
    query = "SELECT * FROM attendance WHERE date=date('now')"

elif filter_type == "Monthly":
    query = "SELECT * FROM attendance WHERE strftime('%m', date)=strftime('%m', 'now')"

elif filter_type == "Yearly":
    query = "SELECT * FROM attendance WHERE strftime('%Y', date)=strftime('%Y', 'now')"


df = pd.read_sql_query(query, conn)

st.dataframe(df)

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "Download CSV",
    csv,
    "attendance_report.csv",
    "text/csv"
)