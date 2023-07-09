import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Agustin Lopez Gasio")
    content = """
    Hi, I am Agustin! I am a new Python programmer. 
    I am looking forward to enter the IT business, 
    focusing more in automations process and cyber-security.
    """
    st.info(content)
