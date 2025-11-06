import streamlit as st
from streamlit_star_rating import st_star_rating
from supabase import create_client, Client, ClientOptions
import postgrest.exceptions

# Supabase setup
supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']
supabase_service_key = st.secrets['SUPABASE_SERVICE_KEY']
supabase: Client = create_client(supabase_url, supabase_key, options=ClientOptions(postgrest_client_timeout=60))


def feedback(user_email, user_name, feedback, user_rating):
    try:
        # Set Supabase session from stored tokens
        if "access_token" in st.session_state and "refresh_token" in st.session_state:
            supabase.auth.set_session(st.session_state["access_token"], st.session_state["refresh_token"])

        # Insert new record (no update logic for multiple reviews)
        supabase.table('user_feedbacks').insert({
            'user_email': user_email,
            'user_name': user_name,
            'feedback': feedback,
            'user_rating': user_rating
        }).execute()
        st.success("Review added successfully ")
    except postgrest.exceptions.APIError as e:
        st.info("You have already submited yor review")
    except Exception as e:
        st.error(f"Connection error: {str(e)}")




def handel_feedback():
    st.header("Give us a review", divider="grey")
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    user_email = st.session_state["user_email"]
    user_name = st.session_state["username"]
    user_rating = st_star_rating("Rate your experience", maxValue=5, defaultValue=5, key="rating")
    user_feedback = st.text_area("Feedback", placeholder="Enter your feedback here")
    button = st.button("Submit Feedback")

    if button:
        if user_email and user_name and user_feedback and user_rating:
            feedback(user_email, user_name, user_feedback, user_rating)
        else:
            st.error("Please fill in all fields.")
