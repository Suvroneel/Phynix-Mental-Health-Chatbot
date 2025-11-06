import streamlit as st

pages = [
    st.Page("pages/1_Chat.py", title="Chat", icon=":material/chat_bubble:"),
    st.Page("pages/2_Home.py", title="Home", icon=":material/home:"),
]

pg = st.navigation(pages)
pg.run()
