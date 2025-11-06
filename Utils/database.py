import os
from supabase import create_client, Client
import streamlit as st
supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']