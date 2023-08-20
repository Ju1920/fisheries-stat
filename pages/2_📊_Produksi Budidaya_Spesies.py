import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(
    page_title="Prod", 
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles/main.css")

st.markdown("## DATA PRODUKSI PERIKANAN BUDIDAYA _KABUPATEN ACEH BARAT 2020-2022_")
st.write("---")

file = pd.read_csv("data/df.csv")

cl = file['Komoditas'].unique().tolist()
tl = file['Jenis'].unique().tolist()
yl = file['Tahun'].unique().tolist()

file['Produksi (Ton)'] = file['Produksi (Ton)']/1000.0

col1, col2, col3 = st.columns(3)

with col1:
    new_cl = st.multiselect('Pilih ikan: ', cl, default = ['Lele', 'Nila'])

with col2:
    new_tl = st.multiselect('Pilih tipe: ', tl, default = ['Kolam Air Tenang', 'Tambak Sederhana'])

with col3:
    year = st.multiselect('Pilih tahun: ', yl, default=[2020, 2021, 2022])

new_ct= (file['Komoditas'].isin(new_cl)) & (file['Jenis'].isin(new_tl)) & (file['Tahun'].isin(year))

st.markdown('###')

with st.container():
    st.write(""" Tabel Produksi Menurut Jenis Ikan  """)
    df1 = file[new_ct].groupby(['Komoditas','Jenis','Tahun'])['Produksi (Ton)'].sum()
    df1 = df1.reset_index()
    st.dataframe(df1, width=1000)

st.markdown('###')

with st.container():
    # st.write(""" Test 2  """)
    ex = df1.groupby('Komoditas')['Produksi (Ton)'].agg('sum')
    ex = ex.reset_index()
    chart = alt.Chart(ex).mark_bar().encode(
        y=alt.Y('Komoditas:N', sort='-x'),
        x='sum(Produksi (Ton))',
        color='Komoditas:N',
    ).interactive()
    st.altair_chart(chart, theme="streamlit", use_container_width=True)


