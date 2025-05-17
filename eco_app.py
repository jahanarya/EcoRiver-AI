
import streamlit as st
import requests
from PIL import Image
import io
import os
from datetime import datetime

# Title and logo
st.set_page_config(page_title="EcoRiver AI", page_icon="🌊", layout="wide")
st.title("🌊 EcoRiver AI – Intelligent River Protection System")
st.caption("Saving Every Drop, Protecting Every River.")

# Sidebar navigation
st.sidebar.title("📁 Navigation")
app_mode = st.sidebar.radio("Go to", ["📊 Dashboard", "📸 Upload Satellite Image", "🛰️ River Analysis", 
                                      "📍 River Map", "📑 PDF Report", "📈 Historical Data", 
                                      "🔔 Alert System", "📬 Feedback"])

# Global state
if "alerts" not in st.session_state:
    st.session_state.alerts = []

# Feature: Upload Satellite Image
if app_mode == "📸 Upload Satellite Image":
    st.header("Upload Satellite Image")
    uploaded_file = st.file_uploader("Upload a satellite image", type=["jpg", "jpeg", "png", "tif"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        with open("uploaded_image.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Image saved!")

# Feature: River Analysis
elif app_mode == "🛰️ River Analysis":
    st.header("Run River Encroachment Detection")
    if os.path.exists("uploaded_image.jpg"):
        st.image("uploaded_image.jpg", caption="Image for Analysis", use_column_width=True)
        if st.button("Run AI Detection"):
            st.info("🧠 Running AI Model... (simulated)")
            st.image("uploaded_image.jpg", caption="Detected Encroachments", use_column_width=True)
            st.success("✅ Encroachment analysis completed!")
            st.session_state.alerts.append(f"🚨 [Alert] Encroachment detected on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.warning("⚠️ Please upload an image first.")

# Feature: Dashboard
elif app_mode == "📊 Dashboard":
    st.header("📊 Real-Time River Monitoring Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Encroachment Cases", "12", "+3 this week")
    col2.metric("Protected Rivers", "8", "+1 this month")
    col3.metric("Live Alerts", len(st.session_state.alerts), "Live")
    st.line_chart({"Encroachments": [2, 5, 7, 6, 9, 12]})

# Feature: River Map
elif app_mode == "📍 River Map":
    st.header("📍 River Geo-Tracking Map")
    st.map()

# Feature: PDF Report
elif app_mode == "📑 PDF Report":
    st.header("📑 Generate Encroachment Report")
    name = st.text_input("Officer Name")
    remarks = st.text_area("Remarks", placeholder="Add any findings or observations...")
    if st.button("Generate PDF"):
        st.success("✅ PDF Generated (simulation)")
        st.download_button("📥 Download Report", data="PDF content here", file_name="encroachment_report.pdf")

# Feature: Historical Data
elif app_mode == "📈 Historical Data":
    st.header("📈 Historical Analysis")
    st.line_chart({"Encroachments": [1, 2, 3, 4, 5, 6, 7]})
    st.bar_chart({"River Width Change": [50, 48, 47, 46, 45, 43]})

# Feature: Alert System
elif app_mode == "🔔 Alert System":
    st.header("🔔 AI-Based Alert System")
    st.subheader("⚠️ Automated Encroachment Alerts")
    if st.session_state.alerts:
        for alert in st.session_state.alerts[::-1]:
            st.warning(alert)
    else:
        st.success("✅ No current alerts.")

# Feature: Feedback
elif app_mode == "📬 Feedback":
    st.header("📬 Submit Feedback")
    name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")
    if st.button("Submit"):
        st.success("🙏 Thank you for your feedback!")
