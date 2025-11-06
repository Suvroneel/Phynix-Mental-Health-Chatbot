# Updated Home Page Code for Project Phynix (with restored sections)

# 1. Install and Import Dependencies
import random

import streamlit as st
from supabase import create_client, Client, ClientOptions

# Custom modules
from Utils import title
from Utils.Progression_Chart import show_last_chat_metrics, session_progress
from Utils.advice import free_advice
from Utils.ashva import ashva_insights
from Utils.sidebar import render_sidebar_logo
from Utils.title import render_main_title, new_tagline, render_custom_header

# 2. Setup Supabase
supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']
supabase: Client = create_client(supabase_url, supabase_key, options=ClientOptions(postgrest_client_timeout=60))

# 3. Restore Session
render_sidebar_logo()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Authentication
if "access_token" in st.session_state and "refresh_token" in st.session_state:
    try:
        supabase.auth.set_session(st.session_state["access_token"], st.session_state["refresh_token"])
    except Exception as e:
        st.error(f"Failed to set session: {str(e)}")
        st.switch_page("Logout.py")
else:
    st.error("No valid user token. Please log in again.")
    st.switch_page("Logout.py")

if "user_email" not in st.session_state:
    st.error("You are not logged in. Redirecting to login...")
    st.switch_page("Logout.py")

# 4. Top Disclaimer
st.markdown("""
    <div style='text-align: center; padding: 8px; font-size: 13px; color: #58d68d;'>
        ⚠️ Not a substitute for professional mental health advice. Consult a professional if needed.
    </div>
""", unsafe_allow_html=True)

# 5. Title and Tagline
col1, col2 = st.columns([1, 4])
with col1:
    st.image('images/sigmund-ljJDx95-6gE-unsplash.png', use_container_width=True, width=100)
with col2:
    render_main_title()

new_tagline()

# 6. Welcome message
st.markdown("<div style='margin-top: 110px;'></div>", unsafe_allow_html=True)
title.render_welcome_message(st.session_state["username"])

st.markdown("""
    <style>
        .fade-in-text {
            text-align: center;
            font-size: 17px;
            font-weight: 500;
            color: #d35400;
            animation: fadeIn 1.2s ease-in-out;
            margin-top: 10px;
        }

        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
    </style>

    <div class="fade-in-text">
        Every journey begins with a small step. Let’s begin yours together.
    </div>
""", unsafe_allow_html=True)

# 7. Stylish "Begin Your Journey" Button Centered
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    journey = st.button("New Chat", icon=":material/stylus_laser_pointer:")

st.markdown("""
    <style>
        .stButton > button {
            background: linear-gradient(90deg, #ff914d, #ff6e40);
            color: white !important;
            padding: 13px 15px;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s ease;
            box-shadow: 0 4px 14px rgba(255, 110, 64, 0.3);
        }

        .stButton > button:hover {
            background: linear-gradient(90deg, #ff6e40, #ff914d);
            box-shadow: 0 6px 18px rgba(255, 110, 64, 0.45);
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

if journey:
    st.switch_page("pages/1_Chat.py")

st.markdown("""
    <style>
        .st-emotion-cache-yinll1 { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# Daily Free Advice
st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
render_custom_header("Your Daily Free Advice")
st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
quote = random.choice(free_advice["bhagavad_gita"])

# Inject custom CSS once (place near top of your app)
# Custom CSS injection (place this once near the top of your Streamlit app)
st.markdown("""
    <style>
        .quote-box {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #f5c49b;
            margin-top: 10px;
            box-shadow: 0 4px 20px rgba(255, 145, 77, 0.35);
        }

        .quote-text {
            text-align: center;
            font-size: 20px !important;
            color: #333333 !important;
            font-family: "Segoe UI", "Helvetica", sans-serif !important;
            font-style: italic;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# Render the quote using HTML block
st.markdown(f"""
<div class="quote-box">
  <p class="quote-text">“{quote}”</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

# Reflection Space
render_custom_header("Ashva Insights")

context_summary = "You've mentioned sleep a few times this week."
# raag_output = "It might help to wind down with less screen time before bed. Would you like some suggestions?"

ashva_insights("calcutta75", "suvroneelnathak@gmail.com")

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
# 9. Dashboard Section
render_custom_header("Dashboard")

show_last_chat_metrics("calcutta75")

st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

session_progress(st.session_state["username"])
