import streamlit as st
from Utils import Progression_Chart
from Utils.ashva import journal
from Utils.profile import prof_change, update_profile, profile_name, show_bio
from Utils.sidebar import render_sidebar_logo
from supabase import create_client, Client, ClientOptions

from Utils.title import render_custom_header, render_custom_subheader

# 1. Setup Supabase
supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']
supabase: Client = create_client(supabase_url, supabase_key, options=ClientOptions(postgrest_client_timeout=60))

# button
st.markdown("""
        <style>
            .stButton > button {
                background: linear-gradient(90deg, #ff914d, #ff6e40);
                color: white !important;
                padding: 13px 10px;
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

# 2. Authentication
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

# button


# 3. Custom CSS for image and button styling
st.markdown("""
    <style>
    /* Style the image to look like a wallpaper/profile */
    .stImage > img {
        max-width: 100%;
        max-height: 400px; /* Adjust height for wallpaper feel */
        width: 100%; /* Fill container width */
        object-fit: cover; /* Scale image to cover the area */
        border-radius: 10px; /* Rounded corners for profile style */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    /* Target button font size specifically */
    .stButton > button.st-emotion-cache-13lcgu3 {
        font-size: 9px !important; /* Set font size to 9px */
        padding: 4px 8px !important; /* Adjust padding for smaller button */
    }
    </style>
""", unsafe_allow_html=True)

# 4. Render sidebar logo
render_sidebar_logo()



# 7. Initialize session state for profile image if not already set
if 'profile_image' not in st.session_state:
    st.session_state.profile_image = "images/profiles/profile1.png"  # Default image path


# 8. Main layout for profile display
col1, col2 = st.columns([4, 1])  # Adjust column widths to push button to the right
with col1:
    st.image(st.session_state.profile_image, width=200)  # Display selected profile image
    profile_name(st.session_state["username"])
    badge = st.badge("Verified ✔", color="green")

with col2:
    if st.button("Edit Profile", icon=":material/draw:"):
        prof_change()

# 9. Spacer
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# 10. About section
show_bio(user_name="calcutta75")

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)


# 11. Define the dialog function for updating profile description

# 12. Update profile button
if st.button("Update bio", icon=":material/draw:"):
    update_profile(st.session_state["username"])

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

# 14. Settings section
render_custom_header("Ashva Diaries")
journal()
colA, colB = st.columns([4, 1])

with colB:

    new_entry = st.button("New Entry", type="tertiary",icon=":material/draw:")

if new_entry:
    st.info("Under development")

# 13. Spacer
st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

# 14. Settings section
render_custom_header("Settings")

col1, col2 = st.columns([4, 1])  # Adjust column widths to push button to the right

with col1:
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    render_custom_subheader("Logout of all sessions")

with col2:
    if st.button("Logout", type="tertiary", icon=":material/logout:"):
        st.session_state.messages = []
        st.session_state.message_submitted = False
        st.switch_page("Logout.py")
