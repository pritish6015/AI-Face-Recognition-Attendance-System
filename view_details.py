import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

if st.sidebar.button("❌ Close"):

    components.html(
        """
        <script>
            window.close();
        </script>
        """,
        height=0,
    )
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Attendance Details",
    layout="centered"
)

st.title("📊 Attendance Details")

# ---------------------------------------------------
# DATABASE
# ---------------------------------------------------

conn = sqlite3.connect(
    "attendance.db",
    check_same_thread=False
)

# ---------------------------------------------------
# GET USER FROM DATABASE
# ---------------------------------------------------

cursor = conn.cursor()

cursor.execute("""
SELECT current_user
FROM system_state
WHERE id = 1
""")

row = cursor.fetchone()

if not row or not row[0]:

    st.error("⚠️ No User Found")

    st.stop()

unique_id = row[0]

cursor.execute("""
SELECT full_name
FROM users
WHERE unique_id = ?
""", (unique_id,))

user = cursor.fetchone()

if not user:

    st.error("⚠️ User not found")

    st.stop()

full_name = user[0]

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

query = f"""
SELECT date, status
FROM attendance
WHERE unique_id='{unique_id}'
ORDER BY date
"""

df = pd.read_sql_query(query, conn)

# ---------------------------------------------------
# SHOW DATA
# ---------------------------------------------------

if df.empty:

    st.warning("No attendance records found.")

else:

    df["date"] = pd.to_datetime(df["date"])

    monthly = (
        df.groupby(df["date"].dt.strftime("%Y-%m"))
        .size()
        .reset_index(name="Attendance Count")
    )

    fig = px.bar(
        monthly,
        x="date",
        y="Attendance Count",
        title=f"{full_name} - Monthly Attendance",
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Attendance Records")

    st.dataframe(
        df,
        use_container_width=True
    )
    # cursor.execute("""
    #     UPDATE system_state
    #     SET current_user = NULL
    #     WHERE id = 1
    #     """)

    # conn.commit()