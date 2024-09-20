import streamlit as st

st.set_page_config(
    page_title="DEDEL",
    page_icon="logo USU.png",
    layout="wide"
)

st.header("Tahapan Tekstur MPASI\n", divider="green")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)