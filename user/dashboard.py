import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px


conn = sqlite3.connect("attendance.db")

user = st.session_state.user

unique_id = user[1]
full_name = user[2]

st.title("User Dashboard")

st.success(f"Welcome {full_name}")

st.info(f"Employee/Student ID: {unique_id}")


df = pd.read_sql_query(
    f"SELECT * FROM attendance WHERE unique_id='{unique_id}'",
    conn
)

st.subheader("Attendance Records")
st.dataframe(df)


if not df.empty:
    st.subheader("Attendance Trend")

    trend = df.groupby("date").size().reset_index(name="count")

    fig = px.bar(
        trend,
        x="date",
        y="count",
        title="Personal Attendance"
    )

    st.plotly_chart(fig, use_container_width=True)