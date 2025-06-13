# pages/9_BLI_08_Akademik.py

import streamlit as st
import sqlite3

def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

def get_supervised_students(penyelia):
    conn = create_connection()
    c = conn.cursor()
    c.execute("""
        SELECT b.no_pelajar, b.nama FROM penyelia_akademik p
        JOIN bli01 b ON p.no_pelajar = b.no_pelajar
        WHERE p.penyelia = ?
    """, (penyelia,))
    results = c.fetchall()
    conn.close()
    return results

def simpan_bli08(no_pelajar, skor_laporan, skor_logbook, skor_tambahan, komen):
    conn = create_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS penilaian_akademik (
            no_pelajar TEXT PRIMARY KEY,
            skor_laporan REAL,
            skor_logbook REAL,
            skor_tambahan REAL,
            komen TEXT
        )
    """)
    c.execute("""
        INSERT OR REPLACE INTO penilaian_akademik
        VALUES (?, ?, ?, ?, ?)
    """, (no_pelajar, skor_laporan, skor_logbook, skor_tambahan, komen))
    conn.commit()
    conn.close()

st.header("🎓 Penilaian Penyelia Akademik (BLI-08)")

nama_penyelia = st.text_input("Nama Anda (Penyelia Akademik)")
kata_laluan = st.text_input("Kata Laluan", type="password")

if kata_laluan == "akademik2025" and nama_penyelia:
    pelajar_list = get_supervised_students(nama_penyelia)

    if pelajar_list:
        pelajar_options = {f"{nama} ({no_pelajar})": no_pelajar for no_pelajar, nama in pelajar_list}
        selected_label = st.selectbox("Pilih Pelajar", list(pelajar_options.keys()))
        no_pelajar = pelajar_options[selected_label]

        st.subheader("📊 Penilaian Laporan Akhir (30%)")
        skor_laporan = st.slider("Markah Laporan", 0, 30, 15)

        st.subheader("📘 Penilaian Buku Log (10%)")
        skor_logbook = st.slider("Markah Buku Log", 0, 10, 5)

        st.subheader("📝 Penilaian Tambahan (30%)")
        skor_tambahan = st.slider("Markah Tambahan", 0, 30, 15)

        komen = st.text_area("Komen Tambahan")

        if st.button("Hantar Penilaian"):
            simpan_bli08(no_pelajar, skor_laporan, skor_logbook, skor_tambahan, komen)
            st.success("Penilaian BLI-08 telah dihantar.")
    else:
        st.info("Tiada pelajar di bawah penyeliaan anda.")
else:
    st.warning("Masukkan nama dan kata laluan untuk akses.")
