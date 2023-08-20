import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(
    page_title="Kapal", 
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles/main.css")

st.markdown("## JUMLAH KAPAL _KABUPATEN ACEH BARAT 2020-2022_")
st.write("---")


file = pd.read_csv("data/df-t2.csv")

cl = file['Kecamatan'].unique().tolist()
tl = file['Jenis'].unique().tolist()
yl = file['Tahun'].unique().tolist()

col1, col2, col3 = st.columns(3)

with col1:
    new_cl = st.multiselect('Pilih kecamatan: ', cl, default = ['Johan Pahlawan', 'Meureubo'])

with col2:
    new_tl = st.multiselect('Pilih jenis budidaya: ', tl, default = ['Kapal motor'])

with col3:
    year = st.multiselect('Pilih tahun: ', yl, default=[2020])

new_ct= (file['Kecamatan'].isin(new_cl)) & (file['Jenis'].isin(new_tl)) & (file['Tahun'].isin(year))

st.markdown('###')

with st.container():
    st.write(""" Tabel Jumlah Kapal Berdasarkan Kecamatan  """)
    df1 = file[new_ct].groupby(['Kecamatan','Jenis','Tahun'])['Jumlah'].sum()
    df1 = df1.reset_index()
    st.dataframe(df1, width=1000)

st.markdown('###')

with st.container():
    # st.write(""" Test 2  """)
    ex = df1.groupby('Kecamatan')['Jumlah'].agg('sum')
    ex = ex.reset_index()
    chart = alt.Chart(ex).mark_bar().encode(
        x='sum(Jumlah):Q',
        y=alt.Y('Kecamatan:N', sort='-x'),
        color='Kecamatan',
    ).interactive()
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
