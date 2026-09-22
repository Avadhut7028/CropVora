import streamlit as st

st.title("🧑‍🔬 Expert Advisory & Crop Selector")

t27, t28 = st.tabs(["27. Expert Consultation", "28. Crop Recommendation"])

with t27:
    st.subheader("Talk to Agri Scientists")
    channels = [
        ("💬 Chat with Agronomist", "Connect over text message with real-time photo sharing[cite: 1]."),
        ("📞 Audio Call with Expert", "Speak in your local language directly with university scientists[cite: 1]."),
        ("📹 Video Consultation", "Show live crop symptoms to plant pathologists via video feed[cite: 1]."),
        ("📅 Book On-Field Inspection", "Schedule an agronomist visit to your farm boundary[cite: 1].")
    ]
    for c_title, c_desc in channels:
        st.markdown(f"""
        <div style="background:white; border-radius:12px; padding:1rem; box-shadow:0 3px 10px rgba(0,0,0,0.05); margin-bottom:0.75rem;">
            <h4 style="margin:0; color:#15803d;">{c_title}</h4>
            <p style="margin:0.25rem 0 0 0; color:#475569;">{c_desc}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Initiate {c_title.split()[1]}", key=c_title)

with t28:
    st.subheader("AI Crop Recommendation Engine")
    season = st.selectbox("Current Sowing Season", ["Kharif", "Rabi", "Zaid"])
    soil_type = st.selectbox("Soil Characteristic", ["Clay Loam", "Black Soil", "Sandy Loam", "Red Soil"])
    water = st.select_slider("Water Availability", ["Scanty", "Medium", "High / Canal"])
    
    if st.button("Get Recommendations"):
        st.markdown("""
        <div style="background:white; padding:1.25rem; border-radius:12px; box-shadow:0 4px 14px rgba(0,0,0,0.05); margin-top:1rem;">
            <h4 style="color:#15803d;">Top Matches for Your Farm:</h4>
            <ol>
                <li><strong>Basmati Rice (Pusa 1121):</strong> High profit margin, fits your clay loam soil.</li>
                <li><strong>Soybean (JS 335):</strong> Good soil rejuvenation, medium water requirement.</li>
                <li><strong>Maize:</strong> Short duration cash crop alternate.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
