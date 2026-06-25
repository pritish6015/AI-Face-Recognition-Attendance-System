import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("attendance.db")

user = st.session_state.user

unique_id = user[1]

query = f"SELECT * FROM attendance WHERE unique_id='{unique_id}'"

attendance_df = pd.read_sql_query(query, conn)

st.dataframe(attendance_df)