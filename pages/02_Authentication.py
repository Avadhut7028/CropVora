import streamlit as st

st.title("🔐 Account Access")

tab_login, tab_register = st.tabs(["5. Welcome Back (Login)", "6. Create Account (Register)"])

with tab_login:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
            <h3 style="color:#15803d; margin-top:0;">Login to continue</h3>
            <p style="color:#64748b;">Access your farm dashboard and crop logs</p>
        </div>
        """, unsafe_allow_html=True)
        
        phone = st.text_input("Mobile Number", placeholder="+91 98765 43210")
        pwd = st.text_input("Password", type="password")
        
        if st.button("Login"):
            st.success("Authenticated successfully!")
            st.switch_page("pages/03_Dashboard.py")
            
        st.button("🌐 Continue with Google", key="g_login")

with tab_register:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("Join Cropvora Today")
        full_name = st.text_input("Full Name", placeholder="Ramesh Patel")
        mobile = st.text_input("Phone Number", placeholder="10-digit number")
        state = st.selectbox("State", ["Gujarat", "Punjab", "Maharashtra", "Haryana", "Madhya Pradesh"])
        crop_focus = st.multiselect("Primary Crops", ["Rice", "Wheat", "Cotton", "Sugarcane", "Soybean"])
        reg_pwd = st.text_input("Create Password", type="password")
        
        if st.button("Register Account"):
            st.success("Account created! Redirecting to dashboard...")
            st.switch_page("pages/03_Dashboard.py")
