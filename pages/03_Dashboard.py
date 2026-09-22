import streamlit as st

st.title("👨‍🌾 Farmer Dashboard")
st.caption("Good Morning, Ramesh! Here is your daily farm summary.")

# Weather Banner
st.markdown("""
<div style="background: linear-gradient(135deg, #15803d 0%, #166534 100%); color: white; padding: 1.5rem; border-radius: 16px; box-shadow: 0 8px 24px rgba(21,128,61,0.25); margin-bottom: 1.5rem;">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
            <h1 style="margin:0; color:white;">30°C</h1>
            <p style="margin:0; opacity:0.9;">Partly Cloudy • Anand, Gujarat</p>
        </div>
        <div style="text-align:right;">
            <p style="margin:0;">💧 60% Humidity</p>
            <p style="margin:0;">💨 12 km/h Wind</p>
            <p style="margin:0;">🌧️ 20% Rain Chance</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Metric Row
c1, c2, c3, c4 = st.columns(4)
c1.metric("Field Moisture", "42%", "+2%")
c2.metric("Mandi Price (Wheat)", "₹2,600/q", "+₹50")
c3.metric("Pending Tasks", "4 Tasks", "Due Today")
c4.metric("Active Crops", "3 Varietals", "Optimal")

col_tasks, col_actions = st.columns([3, 2])

with col_tasks:
    st.subheader("📋 Today's Tasks")
    tasks = [
        ("Irrigation", "Apply 2 hours drip irrigation to Field 2 (Sugarcane)", True),
        ("Fertilizer", "Top-dress Urea (40kg/acre) in Wheat Plot A", False),
        ("Pesticide Spray", "Spray Neem oil 5ml/L for aphid prevention in Cotton", False),
        ("Inspection", "Examine leaf spots on Basmati Rice border", False)
    ]
    for task_type, detail, done in tasks:
        st.markdown(f"""
        <div style="background: white; border-left: 4px solid {'#15803d' if done else '#f59e0b'}; padding: 0.9rem; border-radius: 8px; margin-bottom: 0.6rem; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
            <strong>{task_type}</strong> — {detail}
        </div>
        """, unsafe_allow_html=True)

with col_actions:
    st.subheader("⚡ Quick Actions")
    if st.button("🔍 AI Disease Scan"):
        st.switch_page("pages/06_Tools.py")
    if st.button("📈 Check Market Prices"):
        st.switch_page("pages/06_Tools.py")
    if st.button("🧪 Fertilizer Calculator"):
        st.switch_page("pages/06_Tools.py")
    if st.button("📖 Crop Catalog"):
        st.switch_page("pages/04_Crop_Guide.py")
