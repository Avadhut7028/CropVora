import streamlit as st

st.title("🌾 Crop Catalog & Guide")

t1, t2, t3, t4 = st.tabs(["8. Categories", "9. Crop List", "10. Crop Details", "11. Variety Details"])

with t1:
    st.subheader("Crop Categories")
    cats = ["Cereal Crops", "Pulses", "Oil Seeds", "Vegetables", "Fruits", "Sugar Crops", "Spices", "Fiber Crops"]
    cols = st.columns(4)
    for i, cat in enumerate(cats):
        with cols[i % 4]:
            st.markdown(f"""
            <div style="background:white; border-radius:12px; padding:1.2rem; text-align:center; box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:1rem; border:1px solid #f1f5f9;">
                <span style="font-size:2rem;">🌿</span>
                <p style="font-weight:600; margin-top:0.5rem; color:#1e293b;">{cat}</p>
            </div>
            """, unsafe_allow_html=True)

with t2:
    st.subheader("Select Crop")
    crops = [
        {"name": "Rice (Paddy)", "duration": "120-150 Days", "season": "Kharif", "yield": "20-25 Qtl/Acre"},
        {"name": "Wheat", "duration": "110-130 Days", "season": "Rabi", "yield": "18-22 Qtl/Acre"},
        {"name": "Cotton", "duration": "150-180 Days", "season": "Kharif", "yield": "10-15 Qtl/Acre"},
        {"name": "Sugarcane", "duration": "10-12 Months", "season": "Annual", "yield": "350-400 Qtl/Acre"},
        {"name": "Soybean", "duration": "90-105 Days", "season": "Kharif", "yield": "8-12 Qtl/Acre"},
    ]
    for c in crops:
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.markdown(f"""
            <div style="background:white; padding:1rem; border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.04); margin-bottom:0.5rem;">
                <h4 style="margin:0; color:#15803d;">{c['name']}</h4>
                <p style="margin:0; color:#64748b; font-size:0.85rem;">Cycle: {c['duration']} | Season: {c['season']} | Potential: {c['yield']}</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.button(f"View {c['name'].split()[0]}", key=f"btn_{c['name']}")

with t3:
    st.subheader("Rice (Oryza sativa) - Details")
    st.markdown("""
    <div style="background:white; padding:1.5rem; border-radius:14px; box-shadow:0 4px 15px rgba(0,0,0,0.05); margin-bottom:1rem;">
        <h3 style="color:#15803d; margin-top:0;">Rice Overview</h3>
        <p>Staple cereal grain requiring tropical/subtropical warm humid climates with high soil moisture retention.</p>
        <hr style="border:0; border-top:1px solid #f1f5f9;"/>
        <p><strong>Ideal Soil:</strong> Clayey Loam to Alluvial</p>
        <p><strong>Water Requirement:</strong> 1200 - 1400 mm</p>
        <p><strong>Ideal pH:</strong> 5.5 - 7.0</p>
        <p><strong>Average Yield:</strong> 22-25 Quintals/Acre</p>
    </div>
    """, unsafe_allow_html=True)

with t4:
    st.subheader("Variety Profile: Pusa Basmati 1121")
    st.markdown("""
    <div style="background:white; padding:1.5rem; border-radius:14px; box-shadow:0 4px 15px rgba(0,0,0,0.05);">
        <span class="cv-badge" style="background:#dcfce7; color:#15803d; padding:4px 12px; border-radius:99px; font-weight:bold;">Premium Aroma</span>
        <h3 style="margin-top:0.5rem;">Pusa Basmati 1121</h3>
        <p><strong>Maturity:</strong> 140-145 Days</p>
        <p><strong>Grain Length:</strong> 8.4 mm (Extra Long Slender)</p>
        <p><strong>Yield Potential:</strong> 18-22 Quintals / Acre</p>
        <p><strong>Resistance:</strong> Moderate tolerance to Blast and Bacterial Leaf Blight</p>
    </div>
    """, unsafe_allow_html=True)
