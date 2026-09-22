import streamlit as st

st.title("👤 Account & Configuration")

t23, t24, t25, t26 = st.tabs(["23. Notifications", "24. Profile", "25. Settings", "26. Search"])

with t23:
    st.subheader("Recent Alerts")
    notifs = [
        ("Weather Alert", "High probability of showers tomorrow evening. Postpone urea broadcasting[cite: 1].", "10:00 AM"),
        ("Mandi Update", "Wheat prices rose by ₹50/Quintal in Rajkot mandi[cite: 1].", "08:30 AM"),
        ("Disease Alert", "Yellow rust alerts reported in adjoining district plots.", "Yesterday")
    ]
    for title, msg, time in notifs:
        st.markdown(f"""
        <div style="background:white; padding:1rem; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.04); margin-bottom:0.5rem;">
            <div style="display:flex; justify-content:space-between;">
                <strong>🔔 {title}</strong>
                <span style="color:#94a3b8; font-size:0.8rem;">{time}</span>
            </div>
            <p style="margin:0.25rem 0 0 0; color:#475569;">{msg}</p>
        </div>
        """, unsafe_allow_html=True)

with t24:
    st.subheader("Farmer Profile")
    st.markdown("""
    <div style="background:white; padding:1.5rem; border-radius:14px; box-shadow:0 4px 15px rgba(0,0,0,0.05); text-align:center;">
        <span style="font-size:3.5rem;">👨‍🌾</span>
        <h3 style="margin:0.5rem 0 0 0;">Ramesh Patel</h3>
        <p style="color:#64748b; margin:0;">Registered Farmer ID: #CPV-84920</p>
        <p>Location: Anand, Gujarat • Total Land: 8.5 Acres</p>
    </div>
    """, unsafe_allow_html=True)

with t25:
    st.subheader("App Settings")
    st.selectbox("Language", ["English", "Hindi", "Gujarati", "Punjabi", "Marathi"])
    st.toggle("Push Notifications", value=True)
    st.toggle("SMS Market Price Alerts", value=True)
    st.toggle("Dark Mode Preview", value=False)

with t26:
    st.subheader("Universal Search")
    q = st.text_input("Search crops, diseases, schemes, or tools...")
    if q:
        st.write(f"Search results matching: **{q}**")
