import streamlit as st

st.title("👥 22. Farmer Community Feed")
st.caption("Connect, share field photos, and ask questions with farmers across your region[cite: 1].")

post_text = st.text_input("Share an update or question with the community...")
if st.button("Post Update"):
    st.success("Posted to local community feed!")

posts = [
    {
        "author": "Ramesh Patel • Anand, GJ",
        "time": "2 hours ago",
        "text": "My wheat crop is looking vibrant this year after using balanced bio-fertilizers. Here are the field photos from Plot B[cite: 1]!",
        "likes": 24,
        "comments": 6
    },
    {
        "author": "Sunita Devi • Karnal, HR",
        "time": "5 hours ago",
        "text": "Organic farming gives best results for vegetables. Has anyone tried Trichoderma spray for damping-off in tomato nursery[cite: 1]?",
        "likes": 42,
        "comments": 15
    }
]

for p in posts:
    st.markdown(f"""
    <div style="background:white; border-radius:14px; padding:1.25rem; box-shadow:0 4px 14px rgba(0,0,0,0.05); margin-bottom:1rem; border:1px solid #f1f5f9;">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
            <strong>👨‍🌾 {p['author']}</strong>
            <span style="color:#94a3b8; font-size:0.85rem;">{p['time']}</span>
        </div>
        <p style="color:#334155; margin:0.5rem 0;">{p['text']}</p>
        <div style="color:#15803d; font-size:0.9rem; font-weight:600;">
            👍 {p['likes']} Likes &nbsp; • &nbsp; 💬 {p['comments']} Comments
        </div>
    </div>
    """, unsafe_allow_html=True)
