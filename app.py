import streamlit as st

st.set_page_config(
    page_title="CROPVORA | Smart Farming Hub",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

* {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background-color: #f8fafc;
}

/* Card Container with Soft Elevation Shadow */
.cv-card {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 1.25rem 1.5rem;
    box-shadow: 0 4px 20px -2px rgba(22, 101, 52, 0.08), 0 2px 6px -1px rgba(0, 0, 0, 0.04);
    border: 1px solid #edf2f7;
    margin-bottom: 1rem;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.cv-card:hover {
    box-shadow: 0 8px 25px -4px rgba(22, 101, 52, 0.12);
}

/* Hero Badge */
.cv-badge {
    background-color: #dcfce7;
    color: #15803d;
    font-weight: 600;
    font-size: 0.75rem;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    display: inline-block;
    margin-bottom: 0.5rem;
}

/* Rounded Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #15803d 0%, #166534 100%);
    color: #ffffff;
    border-radius: 10px;
    font-weight: 600;
    border: none;
    padding: 0.6rem 1.25rem;
    box-shadow: 0 4px 10px rgba(21, 128, 61, 0.25);
    transition: all 0.2s ease;
    width: 100%;
}

div.stButton > button:hover {
    background: #166534;
    box-shadow: 0 6px 14px rgba(21, 128, 61, 0.35);
    transform: translateY(-1px);
}
</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

st.title("🌱 Welcome to CROPVORA")
st.caption("Smart Farming Starts Here — All-in-one app for modern agriculture.")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="cv-card">
        <span class="cv-badge">Farm Smarter</span>
        <h3>Digital Agriculture Platform</h3>
        <p>CROPVORA connects crop guides, disease diagnostics, weather tracking, and marketplace intelligence in a single interface.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Enter App (Go to Onboarding)"):
        st.switch_page("pages/01_Onboarding.py")

with col2:
    st.markdown("""
    <div class="cv-card">
        <h4>Quick Navigation</h4>
        <ul>
            <li>Onboarding Screens (1-4)</li>
            <li>Authentication (5-6)</li>
            <li>Dashboard & Diagnostics</li>
            <li>Farm Diary & Expense Manager</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
