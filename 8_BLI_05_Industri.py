# pages/8_BLI_05_Industri.py

import streamlit as st
import sqlite3

def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

def get_pelajar_list():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT no_pelajar, nama FROM bli01")
    results = c.fetchall()
    conn.close()
    return results

def simpan_penilaian(no_pelajar, markah_dict, komen, keputusan):
    conn = create_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS penilaian_industri (
            no_pelajar TEXT PRIMARY KEY,
            keupayaan_mental INTEGER,
            keupayaan_fizikal INTEGER,
            realiabiliti INTEGER,
            tanggungjawab INTEGER,
            komunikasi INTEGER,
            kerja_berpasukan INTEGER,
            inisiatif INTEGER,
            masa_kerja INTEGER,
            kerja_lebih_masa INTEGER,
            kecemasan INTEGER,
            patuh_peraturan INTEGER,
            keseluruhan INTEGER,
            komen TEXT,
            keputusan TEXT
        )
    """)
    c.execute("""
        INSERT OR REPLACE INTO penilaian_industri VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (no_pelajar, *markah_dict.values(), komen, keputusan))
    conn.commit()
    conn.close()

st.header("📝 Penilaian Penyelia Industri (BLI-05)")

penyelia_pass = st.text_input("Kata Laluan Penyelia Industri", type="password")
if penyelia_pass == "industri2025":
    pelajar_list = get_pelajar_list()
    pelajar_options = {f"{nama} ({no_pelajar})": no_pelajar for no_pelajar, nama in pelajar_list}
    selected_label = st.selectbox("Pilih Pelajar", list(pelajar_options.keys()))
    no_pelajar = pelajar_options[selected_label]

    st.subheader("⚙️ Skala Penilaian 1 (Lemah) – 5 (Amat Baik)")
    aspek = [
        "Keupayaan Mental", "Keupayaan Fizikal", "Realiabiliti", "Tanggungjawab",
        "Komunikasi", "Kerja Berpasukan", "Inisiatif", "Masa Kerja",
        "Kerja Lebih Masa", "Kecemasan", "Patuh Peraturan", "Keseluruhan"
    ]
    markah_dict = {}
    for aspek_item in aspek:
        markah_dict[aspek_item.lower().replace(" ", "_")] = st.slider(aspek_item, 1, 5, 3)

    komen = st.text_area("Komen Tambahan")
    keputusan = st.selectbox("Keputusan", ["LULUS", "GAGAL", "TIDAK LENGKAP"])

    if st.button("Hantar Penilaian"):
        simpan_penilaian(no_pelajar, markah_dict, komen, keputusan)
        st.success("Penilaian BLI-05 telah dihantar.")
else:
    st.warning("Sila masukkan kata laluan untuk akses penyelia industri.")
