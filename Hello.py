import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles/main.css")


col1, col2 = st.columns(2)

with col1:
    i1 = Image.open('assets/head_logo.png')
    st.image(i1, width=600)

with col2: 
    st.write("")

st.write("# Selamat datang! 👋")

st.markdown(
    """
    Website ini digunakan untuk penyampaian statistik perikanan Kabupaten Aceh Barat secara interaktif.
    **👈 Pilihan fitur pada menu sisi _(sidebar)_** untuk melihat data yang diinginkan!
    ### Informasi lebih lanjut?
    - :point_right: [Website DKP Aceh Barat](https://dkp.acehbaratkab.go.id/)
    - :point_right: [Instagram DKP Aceh Barat](https://instagram.com/dkp.acehbarat?igshid=MzRIODBiNWFIZA==)
    - :point_right: [Youtube DKP Aceh Barat](https://l.instagram.com/?u=https%3A%2F%2Fyoutube.com%2Fchannel%2FUCNbt7JP6CsXfH5csBGwlIgA&e=AT2i8MKaj4nYsLbe0XNr2TVXg1i5-hTklywGPUcLcMK4XtJRc2CnM0SsoR-Np5WT8DAWn2V4hMbmxThl89jQvVJ6XrjcXMJEiX-xvcmkutjgKRMI)
"""
)