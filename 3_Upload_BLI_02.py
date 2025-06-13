# pages/3_Upload_BLI_02.py

import streamlit as st
import os

UPLOAD_FOLDER = "uploads/bli_02"

def save_uploaded_file(uploaded_file, no_pelajar):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    filepath = os.path.join(UPLOAD_FOLDER, f"BLI-02_{no_pelajar}.pdf")
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath

st.header("📤 Muat Naik BLI-02: Jawapan dari Organisasi")

if "pelajar" in st.session_state:
    no_pelajar = st.session_state["pelajar"][2]
    uploaded_file = st.file_uploader("Sila muat naik fail BLI-02 yang telah disahkan (format PDF)", type=["pdf"])

    if uploaded_file is not None:
        filepath = save_uploaded_file(uploaded_file, no_pelajar)
        st.success(f"Borang BLI-02 berjaya dimuat naik.")
        st.write(f"📄 {filepath}")
else:
    st.warning("Sila log masuk terlebih dahulu.")
