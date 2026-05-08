import streamlit as st
from main import process_emails
import pandas as pd
import os

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Email Automation System",
    page_icon="📧",
    layout="wide"
)

# -----------------------
# CUSTOM CSS (Premium Look)
# -----------------------
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #2c3e50;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
        .success-box {
            background-color: #d4edda;
            padding: 15px;
            border-radius: 10px;
            color: #155724;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.markdown('<p class="title">📧 Email Automation Dashboard</p>', unsafe_allow_html=True)
st.write("Automate and monitor email reminders with one click 🚀")

# -----------------------
# LAYOUT
# -----------------------
col1, col2 = st.columns(2)

# -----------------------
# LEFT SIDE (ACTION)
# -----------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚀 Run Automation")

    if st.button("Send Emails Now"):
        process_emails()
        st.markdown('<div class="success-box">✅ Emails sent successfully!</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# RIGHT SIDE (REPORT)
# -----------------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Latest Report")

    if os.path.exists("outputs/report.csv"):
        df = pd.read_csv("outputs/report.csv")
        st.dataframe(df)
    else:
        st.warning("No report available yet")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.write("💡 Built with Python, FastAPI & Streamlit")