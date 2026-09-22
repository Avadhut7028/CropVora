import streamlit as st

st.title("🏛️ Agri Services & AI Assistant")

t20, t21 = st.tabs(["20. Government Schemes", "21. Cropvora AI Assistant"])

with t20:
    st.subheader("Eligible Subsidies & Central Schemes")
    schemes = [
        ("PM-Kisan Samman Nidhi", "₹6,000/year direct income transfer in 3 equal installments."),
        ("Pradhan Mantri Fasal Bima Yojana (PMFBY)", "Comprehensive crop loss insurance at nominal 1.5% - 2% premium."),
        ("Kisan Credit Card (KCC)", "Concessional institutional credit at 4% interest rate."),
        ("Soil Health Card Scheme", "Free periodic soil testing and macro/micro nutrient recommendations.")
    ]
    for name, desc in schemes:
        st.markdown(f"""
        <div style="background:white; border-radius:12px; padding:1.2rem; box-shadow:0 3px 10px rgba(0,0,0,0.05); margin-bottom:0.75rem;">
            <h4 style="margin:0; color:#15803d;">{name}</h4>
            <p style="margin:0.4rem 0; color:#475569;">{desc}</p>
            <a href="#" style="color:#15803d; font-weight:600; text-decoration:none;">Apply / Learn More →</a>
        </div>
        """, unsafe_allow_html=True)

with t21:
    st.subheader("Ask Cropvora Agronomy AI")
    user_query = st.chat_input("Ask any query about soil, fertilizers, pests...")
    
    if user_query:
        st.chat_message("user").write(user_query)
        st.chat_message("assistant").write(
            f"For optimal response to '{user_query}': Maintain balanced NPK 4:2:1 ratio and always test soil pH before top-dressing nitrogen."
        )
