import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar_header():
    """
    Renders the custom sidebar header for Project Phynix using updated fonts and colors.
    """
    st.sidebar.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Poppins&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.sidebar.markdown(
        "<h1 style='font-family:\"Montserrat\"; color:#B22222;'>Project Phynix</h1>",
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<h4 style='font-family:\"Poppins\"; color: grey; font-weight: 400;'>AI-Powered Mood & Career Tracking</h4>",
        unsafe_allow_html=True
    )

def render_sidebar_logo():

    st.sidebar.title('Project Phynix')
    st.sidebar.image('images/sigmund-ljJDx95-6gE-unsplash.png', use_container_width=False, width=100)

# Utils/config.py


def hide_sidebar():
    """Hides the sidebar and the hamburger menu icon."""
    hide_style = """
           <style>
               /* Hide entire sidebar */
               [data-testid="stSidebar"] {
                   display: none !important;
               }
               /* Hide the hamburger menu */
               [data-testid="collapsedControl"] {
                   display: none !important;
               }
           </style>
       """
    st.markdown(hide_style, unsafe_allow_html=True)



def add_sidebar_tooltip(text="Sidebar Disabled"):
    """Adds a tooltip when hovering over the collapsed sidebar toggle icon."""
    tooltip_css = f"""
    <style>
        /* Target the exact sidebar toggle button */
        [data-testid="stBaseButton-headerNoPadding"]::after {{
            content: "{text}";
            position: absolute;
            top: 100%;
            left: 0;
            background-color: #333;
            color: white;
            padding: 4px 8px;
            font-size: 12px;
            white-space: nowrap;
            border-radius: 4px;
            opacity: 0;
            transform: translateY(5px);
            transition: opacity 0.3s ease;
            pointer-events: none;
            z-index: 9999;
        }}

        [data-testid="stBaseButton-headerNoPadding"]:hover::after {{
            opacity: 1;
        }}
    </style>
    """
    st.markdown(tooltip_css, unsafe_allow_html=True)
