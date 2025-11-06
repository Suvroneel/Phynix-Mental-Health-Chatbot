import streamlit as st
from Utils import Progression_Chart
from Utils.sidebar import render_sidebar_logo
from supabase import create_client, Client, ClientOptions

from Utils.title import render_custom_header, render_custom_subheader

# 1. Setup Supabase
supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']
supabase: Client = create_client(supabase_url, supabase_key, options=ClientOptions(postgrest_client_timeout=60))



#--profile pic --
@st.dialog("Choose your pick")
def prof_change():
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.image("images/profiles/profile1.png", use_container_width=True)
        if st.button("Avatar 1", key="profile1"):
            st.session_state["profile_image"] = "images/profiles/profile1.png"
            st.rerun()
        st.image("images/profiles/profile2.png", use_container_width=True)
        if st.button("Avatar 2", key="profile2"):
            st.session_state["profile_image"] = "images/profiles/profile2.png"
            st.rerun()
        st.image("images/profiles/profile3.png", use_container_width=True)
        if st.button("Avatar 3", key="profile3"):
            st.session_state["profile_image"] = "images/profiles/profile3.png"
            st.rerun()

    with col2:
        st.image("images/profiles/profile4.png", use_container_width=True)
        if st.button("Avatar 4", key="profile4"):
            st.session_state["profile_image"] = "images/profiles/profile4.png"
            st.rerun()
        st.image("images/profiles/profile5.png", use_container_width=True)
        if st.button("Avatar 5", key="profile5"):
            st.session_state["profile_image"] = "images/profiles/profile5.png"
            st.rerun()
        st.image("images/profiles/profile6.png", use_container_width=True)
        if st.button("Avatar 6", key="profile6"):
            st.session_state["profile_image"] = "images/profiles/profile6.png"
            st.rerun()

    with col3:
        st.image("images/profiles/profile7.png", use_container_width=True)
        if st.button("Avatar 7", key="profile7"):
            st.session_state["profile_image"] = "images/profiles/profile7.png"
            st.rerun()
        st.image("images/profiles/profile8.png", use_container_width=True)
        if st.button("Avatar 8", key="profile8"):
            st.session_state["profile_image"] = "images/profiles/profile8.png"
            st.rerun()
        st.image("images/profiles/profile9.png", use_container_width=True)
        if st.button("Avatar 9", key="profile9"):
            st.session_state["profile_image"] = "images/profiles/profile9.png"
            st.rerun()



#profile nmae

def profile_name(username):
    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap" rel="stylesheet">
        <style>
        .custom-welcome {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            font-size: 40px;
            font-weight: 500;
            margin-bottom: 1rem;
        }}
        </style>
        <div class="custom-welcome">{username}</div>
        """,
        unsafe_allow_html=True
    )

#----bio
# Assuming `supabase` is already initialized globally
def show_bio(user_name: str):

    response = supabase.table("user_bio") \
        .select("user_description") \
        .eq("user_name", user_name) \
        .order("created_at", desc=True) \
        .limit(1) \
        .execute()

    bio = response.data[0]['user_description'] if response.data else ""

    if bio:
        st.markdown(f"""
        <i>
            {bio}
        </i>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<i style='color:gray;'>Nothing here yet.</i>", unsafe_allow_html=True)



# 3. Usage

@st.dialog("Update your description")
def update_profile(username: str):
    description = st.text_area("Description", value=st.session_state.get("user_description", ""))

    if st.button("Update"):
        st.session_state["user_description"] = description
        count_response = supabase.table("user_bio").select("id", count="exact").execute()
        next_id = count_response.count + 1

        # Insert into Supabase
        supabase.table("user_bio").insert({
            "id": next_id,

            "user_name": username,
            "user_description": description,
        }).execute()

        st.success("Description saved!")
        st.rerun()

