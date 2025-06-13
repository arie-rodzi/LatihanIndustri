# streamlit_app.py

import streamlit as st

st.set_page_config(
    page_title="Sistem Latihan Industri",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 Sistem Latihan Industri")
st.subheader("Fakulti Sains Komputer & Matematik")
st.markdown("**UiTM Cawangan Negeri Sembilan Kampus Seremban**")

st.markdown("""
Selamat datang ke sistem pengurusan Latihan Industri.

Sila gunakan menu di sebelah kiri untuk:
- Log masuk pelajar
- Isi borang BLI-01
- Muat naik BLI-02
- Isi logbook mingguan
- Hantar laporan akhir
- Disemak oleh penyelia industri & akademik

Sistem ini dibangunkan oleh **Dr. Zahari Md Rodzi**, UiTM Cawangan Negeri Sembilan Kampus Seremban.
""")
