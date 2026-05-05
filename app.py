import streamlit as st
import os

st.set_page_config(layout="wide")

st.markdown("""
<style>

/* Remove ALL scroll globally */
html, body {
    height: 100%;
    overflow: hidden !important;
}

/* Streamlit root containers */
[data-testid="stAppViewContainer"] {
    height: 100vh !important;
    overflow: hidden !important;
}

[data-testid="stAppViewBlockContainer"] {
    padding: 0 !important;
    margin: 0 !important;
    height: 100vh !important;
}

/* Remove any spacing */
.block-container {
    padding: 0rem !important;
}

/* Remove header/footer */
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* Make iframe EXACTLY fit */
iframe {
    height: 100vh !important;
    width: 100% !important;
    border: none !important;
    display: block !important;
}

</style>
""", unsafe_allow_html=True)

# Load your map
map_path = "Digital Soil ATLAS (general).html"

with open(map_path, "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=1000, scrolling=False)