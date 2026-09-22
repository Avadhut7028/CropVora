import streamlit as st

st.title("⚙️ 30. Admin Control Center")
st.caption("Platform governance, user management, and catalog administration[cite: 1].")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Registered Farmers", "1,245", "+18%")
c2.metric("Total Crops", "85 Varietals", "Active")
c3.metric("Daily Diagnoses", "320 Scans", "+12%")
c4.metric("Govt Schemes", "12 Live", "Up to date")

st.markdown("""
<div style="background:white; padding:1.25rem; border-radius:14px; box-shadow:0 4px 14px rgba(0,0,0,0.05); margin-top:1.5rem;">
    <h3>Management Actions</h3>
</div>
""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.button("🌾 Manage Crops Catalog")
    st.button("👥 Manage Farmers & Profiles")
    st.button("📜 Update Government Schemes")
with col_b:
    st.button("🔬 Disease Dataset Classifier")
    st.button("📊 View Platform Analytics")
    st.button("🛠️ System Health & Audit Logs")
