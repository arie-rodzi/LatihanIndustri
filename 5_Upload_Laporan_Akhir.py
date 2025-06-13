# pages/5_Upload_Laporan_Akhir.py

import streamlit as st
import os

UPLOAD_FOLDER = "uploads/laporan_akhir"

def save_laporan_file(uploaded_file, no_pelajar):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    filepath = os.path.join(UPLOAD_FOLDER, f"Laporan_Akhir_{no_pelajar}.pdf")
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath

st.header("📤 Muat Naik Laporan Akhir LI")

if "pelajar" in st.session_state:
    no_pelajar = st.session_state["pelajar"][2]
    uploaded_file = st.file_uploader("Sila muat naik laporan akhir dalam format PDF", type=["pdf"])

    if uploaded_file is not None:
        filepath = save_laporan_file(uploaded_file, no_pelajar)
        st.success("Laporan akhir berjaya dimuat naik.")
        st.write(f"📄 {filepath}")
else:
    st.warning("Sila log masuk terlebih dahulu.")
