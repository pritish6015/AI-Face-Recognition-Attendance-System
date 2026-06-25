import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta


# DATABASE CONNECTION
conn = sqlite3.connect("attendance.db")

attendance_df = pd.read_sql_query(
    "SELECT * FROM attendance",
    conn
)

users_df = pd.read_sql_query(
    "SELECT * FROM users",
    conn
)


# PAGE TITLE
st.title("Attendance Analytics Dashboard")


# =========================
# DASHBOARD METRICS
# =========================

present_today = len(
    attendance_df[
        attendance_df['date'] == datetime.today().strftime('%Y-%m-%d')
    ]
)

late_arrivals = 0

absent_today = max(len(users_df) - present_today, 0)


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Users",
    len(users_df),
    "+5%"
)

col2.metric(
    "Present Today",
    present_today,
    f"{round((present_today/max(len(users_df),1))*100,2)}%"
)

col3.metric(
    "Late Arrivals",
    late_arrivals,
    "0%"
)

col4.metric(
    "Absent Today",
    absent_today,
    f"{round((absent_today/max(len(users_df),1))*100,2)}%"
)


# =========================
# MONTHLY ATTENDANCE RATE
# =========================

st.subheader("Monthly Attendance Rate")

if not attendance_df.empty:

    attendance_df['date'] = pd.to_datetime(attendance_df['date'])

    # attendance_df['month'] = attendance_df['date'].dt.strftime('%b')
    attendance_df['month'] = attendance_df['date'].dt.strftime('%Y-%m')

    monthly_counts = (
        attendance_df
        .groupby('month')
        .size()
        .reset_index(name='attendance_count')
    )

    monthly_counts['attendance_rate'] = (
        monthly_counts['attendance_count'] /
        max(monthly_counts['attendance_count'])
    ) * 100

    fig_line = px.line(
        monthly_counts,
        x='month',
        y='attendance_rate',
        markers=True,
        title='Monthly Attendance Rate (%)'
    )

    fig_line.update_layout(
        xaxis_title='Month',
        yaxis_title='Attendance Rate %',
        template='plotly_dark'
    )

    st.plotly_chart(fig_line, use_container_width=True)


# =========================
# ATTENDANCE DISTRIBUTION
# =========================

st.subheader("Attendance Distribution")

if not attendance_df.empty:

    total_users = len(users_df)

    present_count = present_today

    # late_count = late_arrivals

    absent_count = total_users - present_count


    status_count = pd.DataFrame({
        'status': ['Present', 'Absent'], # 'Late'
        'count': [present_count, absent_count ] #, late_count
    })

    fig_pie = px.pie(
        status_count,
        names='status',
        values='count',
        hole=0.5,
        title='Present vs Absent Distribution'
    )

    fig_pie.update_layout(template='plotly_dark')

    st.plotly_chart(fig_pie, use_container_width=True)


# =========================
# WEEKLY ATTENDANCE RATE
# =========================

st.subheader("Weekly Attendance Rate")

if not attendance_df.empty:

    attendance_df['week'] = attendance_df['date'].dt.isocalendar().week

    weekly = (
        attendance_df
        .groupby('week')
        .size()
        .reset_index(name='count')
    )

    fig_bar = px.bar(
        weekly,
        x='week',
        y='count',
        title='Weekly Attendance Comparison',
        text_auto=True
    )

    fig_bar.update_layout(
        xaxis_title='Week Number',
        yaxis_title='Attendance Count',
        template='plotly_dark'
    )

    st.plotly_chart(fig_bar, use_container_width=True)


# =========================
# DAILY ATTENDANCE TREND
# =========================

st.subheader("Daily Attendance Trend")

if not attendance_df.empty:

    last_7_days = datetime.today() - timedelta(days=7)

    daily_df = attendance_df[
        attendance_df['date'] >= pd.Timestamp(last_7_days)
    ]

    daily_trend = (
        daily_df
        .groupby('date')
        .size()
        .reset_index(name='count')
    )

    fig_area = px.area(
        daily_trend,
        x='date',
        y='count',
        title='Last 7 Days Attendance Trend'
    )

    fig_area.update_layout(
        xaxis_title='Date',
        yaxis_title='Attendance Count',
        template='plotly_dark'
    )

    st.plotly_chart(fig_area, use_container_width=True)


# =========================
# ATTENDANCE HISTORY TABLE
# =========================

st.subheader("Attendance History")


# LAST 30 DAYS FILTER
attendance_df['date'] = pd.to_datetime(attendance_df['date'])

last_30_days = datetime.today() - timedelta(days=30)

attendance_history = attendance_df[
    attendance_df['date'] >= pd.Timestamp(last_30_days)
].copy()


# FORMAT DATE
attendance_history['date'] = attendance_history['date'].dt.strftime('%b %d, %Y')


def color_status(val):

    if str(val).lower() == "present":
        return '''
            background-color: #1e7e34;
            color: white;
            border-radius: 8px;
            padding: 4px;
            font-weight: bold;
            text-align: center;
        '''

    elif str(val).lower() == "late":
        return '''
            background-color: #e0a800;
            color: black;
            border-radius: 8px;
            padding: 4px;
            font-weight: bold;
            text-align: center;
        '''

    elif str(val).lower() == "absent":
        return '''
            background-color: #c82333;
            color: white;
            border-radius: 8px;
            padding: 4px;
            font-weight: bold;
            text-align: center;
        '''

    return ''


attendance_history['status'] = attendance_history['status'].apply(lambda x: x.capitalize())


# METHOD INDICATOR
attendance_history['method'] = "Facial Recognition"


# SELECT CLEAN COLUMNS
attendance_history = attendance_history[
    [
        'date',
        'full_name',
        'unique_id',
        'check_in',
        'status',
        'method'
    ]
]


# RENAME COLUMNS
attendance_history.columns = [
    'Date',
    'Full Name',
    'User ID',
    'Check-In',
    'Status',
    'Method'
]


# =========================
# APPLY COLOR STYLING
# =========================

styled_df = attendance_history.style.map(
    color_status,
    subset=['Status']
)

# DISPLAY STYLED TABLE
st.dataframe(
    styled_df,
    use_container_width=True,
    hide_index=True
)