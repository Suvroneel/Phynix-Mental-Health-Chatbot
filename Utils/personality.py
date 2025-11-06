# test_personality_upload.py

import streamlit as st
from PIL import Image
import os
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
import logging


def upload_personality_image():
    """Handle image upload and display results."""
    st.write("Upload an image to detect facial emotions.")

    uploaded_file = st.file_uploader(
        "Choose an Image file",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        key="personality_image_uploader"  # 👈 Unique key added
    )

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
