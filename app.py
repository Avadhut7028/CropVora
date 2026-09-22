import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CROPVORA - Smart Farming",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- INLINE CSS STYLING (The core request) ---
# We use a markdown string for defining CSS. It applies to all pages.
style_css = """
<style>
/* Global styles for dark/light consistency, but prioritizing a clean light interface */
[data-testid="stAppViewContainer"] {
    background-color: #f8fafc;
}

[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #e2e8f0;
}

/* Common Text Styling */
h1, h2, h3, .stMarkdown, .stText {
    color: #1a202c;
    font-family: 'Inter', sans-serif;
}

/* Card/Container Styling with Shadow (Key requirement) */
.stCard {
    background-color: #FFFFFF;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    border: 1px solid #e2e8f0;
    margin-bottom: 1.5rem;
}

/* Custom shadow class for generic containers */
.shadow-container {
    background-color: #FFFFFF;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 1rem;
}

/* Specific Shadow for smaller items (like cards) */
.shadow-card {
    background-color: #FFFFFF;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    margin-bottom: 0.5rem;
}

/* Custom Shadow for Lists */
.shadow-list-item {
    background-color: #FFFFFF;
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #edf2f7;
    box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    margin-bottom: 0.25rem;
    transition: transform 0.2s ease;
}

.shadow-list-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0,0,0,0.06);
}

/* Custom Green Button Styling */
div.stButton > button {
    background-color: #166534; /* Darker Green from design */
    color: #FFFFFF;
    border-radius: 8px;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    transition: all 0.2s;
    border: none;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #15803d; /* Lighter Hover Green */
    color: #FFFFFF;
    box-shadow: 0 4px 12px rgba(22, 101, 52, 0.3);
}

div.stButton > button:active {
    background-color: #166534;
    transform: translateY(1px);
}

/* Secondary Button styling */
div.stButton > button.secondary {
    background-color: #e2e8f0;
    color: #1a202c;
}
div.stButton > button.secondary:hover {
    background-color: #cbd5e1;
}

/* Form inputs styling */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > select {
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    padding: 0.5rem;
}

/* Progress and Metric colors */
[data-testid="stMetricValue"] {
    color: #166534; /* Green metric color */
}

/* Styling for the login/onboarding screen containers */
.auth-container {
    width: 380px;
    margin: 5rem auto;
    background: #FFFFFF;
    border-radius: 16px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    overflow: hidden;
}

</style>
"""

# Apply the styles
st.markdown(style_css, unsafe_allow_html=True)


# --- APPLICATION LOGIC ---
# Using session state to simulate a login/onboarding flow
if 'is_authenticated' not in st.session_state:
    st.session_state['is_authenticated'] = False

# Simple condition to show login or dashboard
if not st.session_state['is_authenticated']:
    # --- ONBOARDING / LOGIN SIMULATION ---
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.write("## Welcome to CROPVORA")
        
        # Displaying a static image of the onboarding view
        st.image("path/to/image_0.png", caption="CROPVORA All-in-One Farmer App")
        
        st.write("""
        This application is designed to be a complete digital assistant for modern farmers. 
        It integrates AI-powered disease detection, market information, weather updates, 
        and expert advice to help you manage your farm efficiently.
        """)

        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.write("#### Get Started Today")
        if st.button("Simulate Login"):
            st.session_state['is_authenticated'] = True
            st.rerun()  # Forces a re-run to show the dashboard
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- DASHBOARD PAGE REDIRECT ---
    # Streamlit handles multiple pages in the 'pages/' directory automatically.
    # The default behavior will show the contents of this app.py when no page is selected.
    # To mimic a dashboard-first view after login, we will redirect users
    # directly to the Dashboard page when they log in.

    st.switch_page("pages/03_Dashboard.py")

# --- FOOTER ---
st.markdown("---")
st.caption("Powered by CROPVORA AI | 2024")
