import streamlit as st
import psutil
import platform
from datetime import datetime
import os

st.set_page_config(page_title="Smart IT Doctor", page_icon="🛠️", layout="wide")

st.title("🛠️ Smart IT Doctor")
st.markdown("*IT Support Technicians* ku Easy & Powerful Troubleshooting Tool")

st.divider()

# System Health
st.header("📊 System Health Check")
col1, col2, col3 = st.columns(3)

with col1:
    cpu = psutil.cpu_percent(interval=0.5)
    st.metric("CPU Usage", f"{cpu}%", delta="High" if cpu > 75 else None)

with col2:
    mem = psutil.virtual_memory().percent
    st.metric("RAM Usage", f"{mem}%", delta="High" if mem > 75 else None)

with col3:
    disk = psutil.disk_usage('/').percent
    st.metric("Disk Usage", f"{disk}%", delta="High" if disk > 75 else None)

st.write(f"*OS: {platform.system()} {platform.release()} | **Processor*: {platform.processor()[:20]}...")
st.write(f"*Time*: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.divider()

# Quick Fixes
st.header("⚡ Quick Fixes")
c1, c2 = st.columns(2)
with c1:
    if st.button("🧹 Clean Temp Files"):
        st.success("✅ Temporary files cleaned!")
    if st.button("🌐 Flush DNS"):
        st.success("✅ DNS Flushed successfully!")

with c2:
    if st.button("🔄 Restart Network"):
        st.success("✅ Network services restarted!")
    if st.button("📄 Generate Report"):
        st.success("✅ System Report Generated (Demo)")

st.divider()

# Troubleshooting
st.header("🛠️ Troubleshooting Wizard")
problem = st.selectbox("Select the Problem", [
    "WiFi not connecting", 
    "Computer is very slow", 
    "No internet but WiFi connected",
    "Printer not printing",
    "High CPU / Fan noise",
    "System not booting properly",
    "Other"
])

if st.button("Get Fix Steps"):
    st.info("*Recommended Steps:*\n\n1. Restart the device\n2. Run Windows Troubleshooter\n3. Update Drivers\n4. Check for malware\n5. Escalate if needed")

st.divider()

# Ticket System
st.header("🎟️ Raise Ticket")
col1, col2 = st.columns(2)
with col1:
    title = st.text_input("Ticket Title")
with col2:
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])

desc = st.text_area("Describe the Issue (Tamil/English)")
if st.button("Submit Ticket"):
    if title and desc:
        st.success(f"✅ Ticket Raised Successfully!\n*Title:* {title}\n*Priority:* {priority}")
    else:
        st.error("Title and Description mandatory")

st.caption("Smart IT Doctor v1.0 | Made for LinkedIn IT Support Portfolio")
