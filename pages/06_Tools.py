import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🛠️ Precision Farming Tools")

t13, t14, t15, t16, t17 = st.tabs([
    "13. Weather", 
    "14. Market Prices", 
    "15. AI Disease", 
    "16. Fertilizer Calc", 
    "17. Irrigation Calc"
])

with t13:
    st.subheader("Live Forecast (Next 5 Days)")
    days_data = {
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Temp Max (°C)": [32, 33, 31, 30, 29],
        "Humidity (%)": [55, 60, 68, 72, 70],
        "Rain Probability (%)": [10, 15, 60, 45, 20]
    }
    st.dataframe(pd.DataFrame(days_data), use_container_width=True)

with t14:
    st.subheader("Mandi Spot Prices & Trends")
    mandi_df = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Wheat Price (₹/Qtl)": [2550, 2580, 2600, 2590, 2620, 2650, 2600]
    })
    fig = px.line(mandi_df, x="Day", y="Wheat Price (₹/Qtl)", markers=True, title="Wheat Price Trend (This Week)")
    fig.update_traces(line_color='#15803d')
    st.plotly_chart(fig, use_container_width=True)

with t15:
    st.subheader("AI Plant Leaf Disease Diagnostics")
    uploaded_file = st.file_uploader("Upload Leaf Photo", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Analyzed Leaf Image", width=300)
        st.markdown("""
        <div style="background:#fef2f2; border:1px solid #fecaca; padding:1rem; border-radius:10px;">
            <h4 style="color:#b91c1c; margin:0;">Detected: Brown Spot (Bipolaris oryzae)</h4>
            <p style="color:#7f1d1d; margin-top:0.4rem;"><strong>Recommended Treatment:</strong> Spray Mancozeb @ 2.5g/L or Tricyclazole @ 0.6g/L with surfactant.</p>
        </div>
        """, unsafe_allow_html=True)

with t16:
    st.subheader("Fertilizer Dosage Calculator")
    c_area = st.number_input("Field Area (Acres)", value=2.0, step=0.5)
    c_crop = st.selectbox("Crop", ["Rice", "Wheat", "Sugarcane", "Cotton"])
    
    if st.button("Calculate Dosage"):
        urea = c_area * 40
        dap = c_area * 25
        mop = c_area * 20
        st.markdown(f"""
        <div style="background:white; padding:1.25rem; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.05);">
            <h4>Recommended Quantity for {c_area} Acres:</h4>
            <ul>
                <li><strong>Urea (Nitrogen):</strong> {urea:.1f} kg</li>
                <li><strong>DAP (Phosphorus):</strong> {dap:.1f} kg</li>
                <li><strong>MOP (Potash):</strong> {mop:.1f} kg</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with t17:
    st.subheader("Irrigation Water Calculator")
    soil = st.selectbox("Soil Type", ["Clayey Loam", "Sandy Loam", "Black Cotton Soil"])
    irr_area = st.number_input("Field Area (Acres)", value=1.0, step=0.5, key="irr_area")
    
    if st.button("Calculate Water Need"):
        liters = irr_area * 25000
        st.info(f"Estimated Water Requirement: **{liters:,.0f} Liters** per irrigation cycle.")
