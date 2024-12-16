import io

import requests
from PIL import Image

import streamlit as st

# interact with FastAPI endpoint
backend = "http://speechgpt:8000/info"


def process(server_url: str):

    r = requests.get(
        server_url, timeout=8000
    )

    return r


if st.button("Get segmentation map"):
    segments = process(backend)
    st.write(segments)
