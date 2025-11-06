# --- Streamlit Config ---
import streamlit as st

import warnings
import logging




def set_config():
    # 🔇 Suppress all warnings
    warnings.filterwarnings("ignore")

    # 🔇 Suppress Streamlit-specific logs
    logging.getLogger("streamlit.runtime.state.session_state_proxy").setLevel(logging.ERROR)
    logging.getLogger("streamlit").setLevel(logging.ERROR)


    st.set_page_config(
        page_title="Project Phynix",
        page_icon="favicon_io/Project_Phynix_icon_500x500.png",
        layout="centered",
        initial_sidebar_state="collapsed",

    )





























