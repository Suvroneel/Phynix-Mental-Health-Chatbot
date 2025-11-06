import streamlit as st
from supabase import create_client, Client

from Main_Profile import supabase


@st.dialog("Wait a moment")
def create_account(email, password, username):
    try:
        # Step 1: Register with Supabase Auth
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {
                    "display_name": username
                }
            }
        })

        user = response.user
        if user is not None:
            # Step 2: Temporarily skip custom table insert
            supabase.table("user_credentials").insert({
                "user_name": username,
                "email": email,
            }).execute()

            with st.dialog("Account Created"):
                st.write(
                    "Your account has been successfully created. To complete your registration, "
                    "please verify your email address using the confirmation link sent to your inbox."
                )
        else:
            st.error("Signup failed. Supabase did not return a user.")
    except Exception as e:
        st.error(f"Signup failed: {e}")

#usernamesession
def store_session(user, session):
    st.session_state["user"] = user
    st.session_state["session"] = session
    st.session_state["logged_in"] = True


def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        user = response.user
        if user is not None:
            store_session(user, response.session)
            st.success("Login successful!")
            return user
        st.error("Login failed. Please check your credentials.")
        return None
    except Exception as e:
        st.error(f"Login failed: {e}")
        return None