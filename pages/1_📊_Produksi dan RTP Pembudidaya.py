import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(
    page_title="Prod-RTP", 
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles/main.css")

st.markdown("## JUMLAH RTP DAN PRODUKSI PERIKANAN BUDIDAYA _KABUPATEN ACEH BARAT 2015-2022_")
st.write("---")

file = pd.read_csv("data/df2.csv")

cl = file['Kecamatan'].unique().tolist()
tl = file['Jenis'].unique().tolist()
yl = file['Tahun'].unique().tolist()

file['Produksi (Ton)'] = file['Produksi (Ton)']/1000.0

col1, col2, col3 = st.columns(3)

with col1:
    new_cl = st.multiselect('Pilih kecamatan: ', cl, default = ['Samatiga', 'Meureubo'])

with col2:
    new_tl = st.multiselect('Pilih jenis budidaya: ', tl, default = ['Kolam Air Tawar', 'Tambak'])

with col3:
    year = st.multiselect('Pilih tahun: ', yl, default=[2015, 2022])

new_ct= (file['Kecamatan'].isin(new_cl)) & (file['Jenis'].isin(new_tl)) & (file['Tahun'].isin(year))

st.markdown('###')

with st.container():
    st.write(""" Tabel Jumlah Rumah Tangga Perikanan dan Produksi Berdasarkan Kecamatan  """)
    df1 = file[new_ct].groupby(['Kecamatan','Jenis','Tahun'])['RTP', 'Produksi (Ton)'].sum()
    df1 = df1.reset_index()
    st.dataframe(df1, width=1000)

st.markdown('###')

with st.container():
    ex = df1.groupby('Kecamatan')['RTP'].agg('sum')
    ex = ex.reset_index()
    chart = alt.Chart(ex).mark_bar().encode(
        x='sum(RTP):Q',
        y=alt.Y('Kecamatan:N', sort='-x'),
        color='Kecamatan',
    ).interactive()
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

st.markdown('####')

with st.container():
    ex = df1.groupby('Kecamatan')['Produksi (Ton)'].agg('sum')
    ex = ex.reset_index()
    chart = alt.Chart(ex).mark_bar().encode(
        x='sum(Produksi (Ton)):Q',
        y=alt.Y('Kecamatan:N', sort='-x'),
        color='Kecamatan',
    ).interactive()
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

st.markdown('#')

# with st.container():
#     chart = alt.Chart(df1, title='Title ').mark_bar(
#         opacity=1,
#         ).encode(
#         column = alt.Column('Tahun', spacing = 5, header = alt.Header(labelOrient = "bottom")),
#         x =alt.X('Kecamatan', sort='x' ,  axis=None),
#         y =alt.Y('Produksi:Q'),
#         color= alt.Color('Kecamatan')
#         )
#     st.altair_chart(chart, theme="streamlit", use_container_width=True)
