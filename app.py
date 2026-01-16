import streamlit as st

# Load CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Smart Medicine Manager",
    page_icon="💊",
    layout="wide"
)

load_css()

st.sidebar.success("Select a page above 👆")
