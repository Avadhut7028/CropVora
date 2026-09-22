import streamlit as st

st.markdown("""
<style>
.onboard-step {
    text-align: center;
    padding: 2.5rem 1.5rem;
    border-radius: 20px;
    background: #ffffff;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
    border: 1px solid #f1f5f9;
}
.onboard-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🌱 CROPVORA Onboarding")

slides = [
    {
        "icon": "🌾",
        "title": "CROPVORA",
        "subtitle": "Smart Farming Starts Here",
        "desc": "All-in-one digital companion designed specifically for farmers to increase yield and maximize profit."
    },
    {
        "icon": "📖",
        "title": "Complete Crop Guide",
        "subtitle": "Knowledge at your fingertips",
        "desc": "Get detailed step-by-step information about crop varieties, sowing calendars, and optimal production techniques."
    },
    {
        "icon": "🔍",
        "title": "AI Disease Detection",
        "subtitle": "Instant leaf diagnosis",
        "desc": "Snap a photo of crop leaves to diagnose diseases instantly and receive targeted chemical and biological treatments."
    },
    {
        "icon": "⛅",
        "title": "Weather & Market Updates",
        "subtitle": "Real-time updates",
        "desc": "Live micro-weather alerts, APMC mandi spot prices, and trend indicators to make informed decisions."
    }
]

if "step" not in st.session_state:
    st.session_state.step = 0

curr = slides[st.session_state.step]

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f"""
    <div class="onboard-step">
        <div class="onboard-icon">{curr['icon']}</div>
        <h2 style="color: #15803d; margin-bottom: 4px;">{curr['title']}</h2>
        <h4 style="color: #64748b; font-weight: 500;">{curr['subtitle']}</h4>
        <p style="color: #475569; margin-top: 1rem;">{curr['desc']}</p>
        <p style="color: #15803d; font-weight: 700; margin-top: 1.5rem;">Step {st.session_state.step + 1} of 4</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.session_state.step > 0:
            if st.button("⬅️ Previous"):
                st.session_state.step -= 1
                st.rerun()
    with c2:
        if st.session_state.step < 3:
            if st.button("Next ➡️"):
                st.session_state.step += 1
                st.rerun()
        else:
            if st.button("Get Started ✅"):
                st.switch_page("pages/02_Authentication.py")
