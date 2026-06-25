# file: quick_attendance.py

import streamlit as st
import subprocess
import socket
import time
import sqlite3
import pandas as pd
from datetime import datetime
import plotly.express as px
from streamlit.components.v1 import html
import platform

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Quick Attendance Portal",
    layout="centered"
)

st.title("🎯 Smart Attendance System")

# ---------------------------------------------------
# DATABASE
# ---------------------------------------------------

conn = sqlite3.connect("attendance.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "attendance_marked" not in st.session_state:
    st.session_state.attendance_marked = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# ---------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------

def get_latest_attendance():
    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        SELECT unique_id, full_name
        FROM attendance
        WHERE date=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (today,)
    )

    return cursor.fetchone()


def show_chart(unique_id, full_name):

    query = f"""
    SELECT date, status
    FROM attendance
    WHERE unique_id='{unique_id}'
    ORDER BY date
    """

    df = pd.read_sql_query(query, conn)

    if df.empty:
        st.warning("No attendance records found.")
        return

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

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Attendance Records")
    st.dataframe(df, use_container_width=True)

def is_port_running(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex(("localhost", port))

    s.close()

    return result == 0

def run_in_new_terminal(command):

    system = platform.system()

    # WINDOWS
    if system == "Windows":

        subprocess.Popen(
            [
                "cmd",
                "/c",
                "start",
                "cmd",
                "/k",
                command
            ]
        )

    # LINUX
    elif system == "Linux":

        subprocess.Popen(
            [
                "gnome-terminal",
                "--",
                "bash",
                "-c",
                command
            ]
        )

    # MAC
    elif system == "Darwin":

        subprocess.Popen(
            [
                "osascript",
                "-e",
                f'tell app "Terminal" to do script "{command}"'
            ]
        )

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
            
/* Remove Streamlit default padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main Wrapper */
.main-container {
    width: 50%;
    margin-left: auto;
    margin-right: auto;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 40px;
    color: white;
}

/* Success Box */
.success-box {
    background-color: #052e16;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #16a34a;
    margin-top: 20px;
    color: white;
    font-size: 18px;
}


/* ALL BUTTONS BASE STYLE */
div.stButton > button {
    width: 100%;
    border: none;
    color: white;
    font-weight: 600;
    transition: 0.3s ease;
}

/* VIEW DETAILS BUTTON */
button[kind="primary"] {
    height: 80px !important;
    font-size: 20px !important;
    border-radius: 18px !important;

    background: linear-gradient(
        135deg,
        #059669,
        #047857
    ) !important;
}

/* ADMIN LOGIN BUTTON */
button[kind="tertiary"] {
    height: 80px !important;
    font-size: 20px !important;
    border-radius: 18px !important;

    background: linear-gradient(
        135deg,
        #dc2626,
        #991b1b
    ) !important;
}

/* Hover */
div.stButton > button:hover {
    transform: scale(1.02);
    opacity: 0.95;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 40px;
    color: gray;
    font-size: 14px;
}

/* Mobile Responsive */
@media (max-width: 1000px) {

    .main-container {
        width: 90%;
    }

}

</style>
""", unsafe_allow_html=True)
# ---------------------------------------------------
# LOAD BOOTSTRAP ICONS
# ---------------------------------------------------

st.markdown("""
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
""", unsafe_allow_html=True)

# ---------------------------------------------------
# CAMERA BUTTON
# ---------------------------------------------------

camera_clicked = st.button(
    " ",
    use_container_width=True,
    type="secondary"
)

# ---------------------------------------------------
# CAMERA BUTTON CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* START CAMERA BUTTON */
button[kind="secondary"] {

    height: 400px !important;
    border-radius: 28px !important;

    background: linear-gradient(135deg, #1e293b, #0f172a);

    font-size: 0px !important;
    position: relative;
    border: none !important;
}

/* CAMERA ICON */
button[kind="secondary"]::before {

    content: "\\F220";   /* Bootstrap camera icon */

    font-family: "bootstrap-icons" !important;

    font-size: 90px;
    color: white;

    position: absolute;

    top: 50%;
    left: 50%;

    transform: translate(-50%, -50%);
}

/* HOVER EFFECT */
button[kind="secondary"]:hover {

    transform: scale(1.02);
    transition: 0.3s ease;
}

</style>
""", unsafe_allow_html=True)
with st.container():

    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    # ---------------------------------------------------
    # START CAMERA SECTION
    # ---------------------------------------------------
    st.markdown('<div class="camera-button">', unsafe_allow_html=True)
    if camera_clicked:

        subprocess.run(["python", "recognition/recognize.py"])

        latest = get_latest_attendance()

        if latest:

            unique_id = latest[0]
            full_name = latest[1]

            st.session_state.attendance_marked = True

            st.session_state.current_user = {
                "unique_id": unique_id,
                "full_name": full_name
            }

            st.markdown(
                f"""
                <div class="success-box">
                    ✅ Attendance marked successfully for <b>{full_name}</b>
                </div>
                """,
                unsafe_allow_html=True
            )
            cursor.execute(
                """
                UPDATE system_state
                SET current_user=?
                WHERE id=1
                """,
                (unique_id,)
            )

            conn.commit()

        else:
            st.error("❌ Attendance not marked")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------------------------------------------
    # SECOND ROW BUTTONS
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    # ---------------------------------------------------
    # VIEW DETAILS
    # ---------------------------------------------------

    with col1:

        if st.button(
            "📊 View Attendance Details",
            use_container_width=True,
            type="primary"
        ):

            # Attendance already marked
            if st.session_state.attendance_marked:

                # Start details page if not running
                if not is_port_running(8503):

                    run_in_new_terminal("streamlit run view_details.py --server.port 8503")
                    time.sleep(3)

                import streamlit.components.v1 as components

                components.html(
                    """
                    <script>
                        window.open(
                            'http://localhost:8503',
                            '_blank'
                        );
                    </script>
                    """,
                    height=0,
                )

            else:

                st.error("⚠️ Attendance not marked yet")

                st.info("🔐 Redirecting to Login Page...")

                # Start app.py automatically
                if not is_port_running(8501):

                    run_in_new_terminal("streamlit run view_details.py --server.port 8503")
                    time.sleep(3)

                import streamlit.components.v1 as components

                components.html(
                    """
                    <script>
                        window.open(
                            'http://localhost:8503',
                            '_blank'
                        );
                    </script>
                    """,
                    height=0,
                )

    # ---------------------------------------------------
    # ADMIN LOGIN
    # ---------------------------------------------------

    with col2:

        if st.button(
            "🔐 Admin Login",
            use_container_width=True,
            type="tertiary"
        ):

            # Start app.py automatically if not running
            if not is_port_running(8501):

                run_in_new_terminal("streamlit run app.py --server.port 8501")
                time.sleep(3)

            import streamlit.components.v1 as components

            components.html(
                """
                <script>
                    window.open(
                        'http://localhost:8501',
                        '_blank'
                    );
                </script>
                """,
                height=0,
            )
    # ---------------------------------------------------
    # FOOTER
    # ---------------------------------------------------

    st.markdown(
        """
        <div class="footer">
            AI Powered Smart Attendance System
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)