import streamlit as st

st.title("🌾 12. Rice Production Steps")
st.caption("Standard operational agronomy lifecycle from land preparation to harvest.")

steps = [
    ("1. Land Preparation", "Plow twice, puddle thoroughly, and level field evenly to ensure uniform flood irrigation."),
    ("2. Seed Selection", "Select certified seeds with >85% germination rate and soak in brine to discard floaters."),
    ("3. Seed Treatment", "Treat with Carbendazim (2g/kg) or Trichoderma viride to prevent seed-borne fungal infections."),
    ("4. Sowing / Nursery", "Raise nursery beds with adequate compost; maintain wet-nursery moisture."),
    ("5. Irrigation Management", "Maintain 2-3 cm shallow standing water during early tillering; drain before harvest."),
    ("6. Weeding", "Cono-weed at 20 & 40 DAT or apply Pre-emergence herbicide like Pretilachlor within 3 days."),
    ("7. Pest Control", "Monitor for Stem Borer and Brown Plant Hopper using pheromone traps."),
    ("8. Disease Control", "Watch for Sheath Blight and Blast; spray Hexaconazole if threshold crossed[cite: 1]."),
    ("9. Harvesting", "Harvest when 80-85% grains turn golden-yellow and moisture content reaches 20%[cite: 1].")
]

for title, desc in steps:
    st.markdown(f"""
    <div style="background: white; border-radius: 12px; padding: 1.1rem; box-shadow: 0 3px 10px rgba(0,0,0,0.04); margin-bottom: 0.75rem; border-left: 5px solid #15803d;">
        <h4 style="margin: 0; color: #15803d;">{title}</h4>
        <p style="margin: 0.4rem 0 0 0; color: #475569; font-size: 0.95rem;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)
