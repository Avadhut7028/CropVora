import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📊 Farm Management")

t18, t19 = st.tabs(["18. Farm Diary", "19. Expense Manager"])

with t18:
    st.subheader("Today's Field Activity Entry")
    date = st.date_input("Date")
    action_type = st.selectbox("Operation Type", ["Irrigation", "Spraying", "Fertilization", "Weeding", "Harvest"])
    notes = st.text_area("Field Notes / Observations", placeholder="Applied second dose of nitrogen, field looks healthy.")
    
    if st.button("Save Diary Log"):
        st.success("Log saved to farm records!")

with t19:
    st.subheader("Expense Breakdown (Kharif Season)")
    
    exp_data = pd.DataFrame({
        "Category": ["Fertilizers", "Seeds", "Pesticides", "Labor", "Diesel/Machinery"],
        "Amount": [12450, 6500, 4800, 15000, 8200]
    })
    
    fig = px.pie(exp_data, values="Amount", names="Category", title="Cost Distribution", hole=0.45,
                 color_discrete_sequence=px.colors.sequential.Greens_r)
    st.plotly_chart(fig, use_container_width=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Expenses", "₹46,950")
    c2.metric("Projected Revenue", "₹1,25,000")
    c3.metric("Estimated Net Profit", "₹78,050", "+14%")
