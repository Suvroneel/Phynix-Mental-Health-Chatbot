import streamlit as st




def render_main_title():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.markdown("""
        <h1 style='font-family:"Montserrat"; color:#B22222; font-size: 48px;'>
            Project Phynix
        </h1>
    """, unsafe_allow_html=True)


def render_tagline():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.markdown("""
        <h3 style='font-family:"Poppins"; color:#666; font-weight: 400; margin-top:-15px;'>
            AI-Powered Mood & Career Tracking Platform
        </h3>
    """, unsafe_allow_html=True)


def render_full_header():
    render_main_title()
    render_tagline()


#---test-----

render_full_header()
