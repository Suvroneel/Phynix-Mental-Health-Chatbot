import streamlit as st
import re
from Utils import title
import postgrest.exceptions # type: ignore
from supabase import create_client, Client # type: ignore

from Utils.footer import render_footer
from Utils.sidebar import hide_sidebar, add_sidebar_tooltip
from Utils.title import render_main_title, render_tagline

#st.set_page_config(page_title=None, page_icon="images/sigmund-ljJDx95-6gE-unsplash.png", )
st.set_page_config(
    page_title="Phynix",
    page_icon='images/icons/favicon.ico',
    initial_sidebar_state="collapsed"
)
    # Sidebar
hide_sidebar()
add_sidebar_tooltip()

col1, col2 = st.columns([1, 4])
with col1:
    st.image('images/sigmund-ljJDx95-6gE-unsplash.png', use_container_width=True, width=100)
with col2:
    render_main_title()
    render_tagline()
# App Title + Footer Style

# Inject custom CSS for button styling, footer style, and centered "or" divider
st.markdown("""
    <style>
        .st-emotion-cache-yinll1 { display: none !important; }
        .stButton > button {
            width: 100%;  /* Match button width to text input */
            text-align: center;  /* Center button text */
            margin: 10px 0;  /* Add vertical spacing for buttons */
        }
        .google-button {
            background-color: #4285F4;  /* Google blue */
            color: white;
            border: none;
            transition: background-color 0.2s;
        }
        .google-button:hover {
            background-color: #357ae8;  /* Darker blue on hover */
        }
        .or-divider {
            display: flex;
            align-items: center;
            text-align: center;
            margin: 15px 0;
            color: #555;
            font-size: 14px;
            font-family: 'Inter', sans-serif;
        }
        .or-divider::before,
        .or-divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid #ccc;
        }
        .or-divider span {
            padding: 0 10px;
        }
        .form-box {
            max-width: 500px;  /* Constrain form width for better alignment */
            margin: 0 auto;  /* Center the form */
        }
    </style>
""", unsafe_allow_html=True)

# Supabase clients
supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']
supabase: Client = create_client(supabase_url, supabase_key)

# Service role client for bypassing RLS
supabase_service_url = st.secrets['SUPABASE_URL']
supabase_service_key = st.secrets['SUPABASE_SERVICE_KEY']
supabase_service: Client = create_client(supabase_service_url, supabase_service_key)


# Session storage
@st.fragment()
def store_session(user, session):
    st.session_state["user"] = user
    st.session_state["session"] = session
    st.session_state["logged_in"] = True
    st.session_state["user_email"] = user.email
    st.session_state["username"] = user.user_metadata.get("display_name", user.email)


# Insert into user_credentials
@st.fragment()
def insert_credentials(user_email, user_name):
    try:
        # Get current row count
        response = supabase_service.table('user_credentials').select('user_id', count='exact').execute()
        row_count = response.count if response.count is not None else 0
        new_user_id = row_count + 1

        # Insert with computed user_id
        supabase_service.table('user_credentials').insert({
            'user_id': new_user_id,
            'email': user_email,
            'user_name': user_name,
        }).execute()
    except postgrest.exceptions.APIError as e:
        st.error(f"Error submitting credentials: {e.message}")
    except Exception as e:
        st.error(f"Connection error: {str(e)}")


# Login
@st.fragment()
def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        user = response.user
        if user:
            store_session(user, response.session)
            st.session_state["access_token"] = response.session.access_token
            st.session_state["refresh_token"] = response.session.refresh_token
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.switch_page("pages/1_Chat.py")
            #st.switch_page("pages/1_Home - Project_Phynix.py")
        st.error("Login failed. Please check your credentials.")
        return None
    except Exception as e:
        st.error(f"Login failed: {e}")
        return None


# Signup
@st.fragment()
def create_account(email, password, username):
    try:
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
        session = response.session
        if user is not None:
            store_session(user, session)
            st.markdown(
                f"""
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap" rel="stylesheet">
                <style>
                .custom-welcome {{
                    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
                    font-size: 20px;
                    font-weight: 400;
                    color: #88E788;
                    margin-bottom: 1rem;
                }}
                </style>
                <div class="custom-welcome">Account Created Successfully, {username}.<br>Please check your email to verify your account.</div>
                """,
                unsafe_allow_html=True
            )
            try:
                insert_credentials(email, username)
            except Exception as e:
                st.error(f"Insert failed: {e}")
            st.write("Didn't receive the email? Check your spam folder or try again in a few minutes.")
        else:
            st.error("Signup failed. Supabase did not return a user.")
    except Exception as e:
        st.error(f"Signup failed: {e}")

col1, col2 = st.columns([1, 4])  # Adjust column widths to push button to the right
# Main UI




tab1, tab2 = st.tabs([" Login", " Signup"])

# Login Form
with tab1:
    with st.container():
        st.markdown('<div class="form-box">', unsafe_allow_html=True)
        st.subheader("Welcome back!")
        contact_input_email = st.text_input("Email", key="user_email_input")
        contact_input_password = st.text_input("Password", type="password", key="user_password", placeholder="")
        if st.button("Login"):
            if contact_input_email and contact_input_password:
                if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", contact_input_email):
                    login_user(contact_input_email, contact_input_password)
                else:
                    st.error("Invalid email format (e.g., name@domain.com)")
            else:
                st.error("Please complete all required fields before proceeding.")
       # st.markdown('<div class="or-divider"><span>or</span></div>', unsafe_allow_html=True)

        #if st.button("Login with Google"):
            #st.info("Under development")

# Signup Form
with tab2:
    with st.container():
        st.markdown('<div class="form-box">', unsafe_allow_html=True)
        st.subheader("Create an Account")
        new_username = st.text_input("Username (no white spaces) :red[*]", key="signup_username")
        new_email = st.text_input("Email", key="signup_email")
        new_password = st.text_input("Password :red[*]", type="password", key="new_password")
        confirm_password = st.text_input("Confirm Password :red[*]", type="password", key="confirm_password")
        if st.button("Verify Your Email"):
            if not all([new_username, new_email, new_password, confirm_password]):
                st.error("Please complete all required fields.")
            elif re.search(r"\s", new_username):
                st.error("Username must not contain spaces.")
            elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", new_email):
                st.error("Invalid email format (e.g., name@domain.com).")
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            else:
                create_account(new_email, new_password, new_username)

        #st.markdown('<div class="or-divider"><span>or</span></div>', unsafe_allow_html=True)

        #if st.button("Signup with Google"):
            #st.info("Under development")

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
st.write("Please reload if you see any errors or bugs")
render_footer()
