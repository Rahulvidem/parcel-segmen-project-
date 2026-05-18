import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Parcl Buyer Intelligence",
    page_icon="🏢",
    layout="wide"
)

# Hide Streamlit branding for clean full-screen look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
""", unsafe_allow_html=True)

# Load and render the HTML dashboard
with open("parcl_dashboard.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1000, scrolling=True)
