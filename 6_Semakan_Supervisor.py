# pages/6_Semakan_Supervisor.py

import streamlit as st
import sqlite3
import os

def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

def get_logbook_all():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT no_pelajar, minggu, tarikh, aktiviti FROM logbook ORDER BY no_pelajar, minggu")
    result = c.fetchall()
    conn.close()
    return result

def get_laporan(no_pelajar):
    path = f"uploads/laporan_akhir/Laporan_Akhir_{no_pelajar}.pdf"
    return path if os.path.exists(path) else None

def get_bli01_info(no_pelajar):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT nama FROM bli01 WHERE no_pelajar=?", (no_pelajar,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "-"

st.header("🧑‍🏫 Semakan Penyelia: Logbook dan Laporan Akhir")

password = st.text_input("Kata Laluan Penyelia", type="password")
if password == "penyelia2025":  # kata laluan contoh
    st.success("Akses dibenarkan.")

    st.subheader("📘 Logbook Semua Pelajar")
    data = get_logbook_all()
    grouped = {}
    for no_pelajar, minggu, tarikh, aktiviti in data:
        grouped.setdefault(no_pelajar, []).append((minggu, tarikh, aktiviti))

    for no_pelajar, entries in grouped.items():
        nama = get_bli01_info(no_pelajar)
        st.markdown(f"### {nama} ({no_pelajar})")
        for m, t, a in entries:
            st.markdown(f"**Minggu {m}** ({t}):

{a}
---")

    st.subheader("📄 Laporan Akhir Pelajar")
    for no_pelajar in grouped:
        path = get_laporan(no_pelajar)
        if path:
            nama = get_bli01_info(no_pelajar)
            with open(path, "rb") as file:
                st.download_button(f"📥 Muat Turun Laporan: {nama}", file, file_name=os.path.basename(path))
else:
    st.warning("Masukkan kata laluan untuk akses.")
