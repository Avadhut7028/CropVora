import streamlit as st
import pandas as pd

st.title("🗺️ 29. My Farm Map & Boundary")
st.caption("Satellite view, plot segmentation, and soil sampling markers[cite: 1].")

farm_plots = pd.DataFrame({
    "lat": [22.5645, 22.5655, 22.5638],
    "lon": [72.9289, 72.9300, 72.9295]
})

st.map(farm_plots, zoom=15)

st.markdown("""
<div style="background:white; padding:1.25rem; border-radius:14px; box-shadow:0 4px 14px rgba(0,0,0,0.05); margin-top:1.5rem;">
    <h4>Field Survey Details</h4>
    <p><strong>Total Geo-Fenced Area:</strong> 8.5 Acres</p>
    <p><strong>Field 1:</strong> 4.0 Acres (Rice - Vegetative Stage)</p>
    <p><strong>Field 2:</strong> 2.5 Acres (Sugarcane - Maturing)</p>
    <p><strong>Field 3:</strong> 2.0 Acres (Fallow / Green Manuring)</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.button("📐 Re-measure Bounds")
c2.button("🧪 Log Soil Sample")
c3.button("🛰️ Vegetation Index (NDVI)")
