# pages/7_Admin_Panel.py

import streamlit as st
import sqlite3
import os

def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

def get_students_by_program(program_code):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT no_pelajar, nama, program FROM bli01 WHERE program LIKE ?", (f"%{program_code}%",))
    results = c.fetchall()
    conn.close()
    return results

def update_supervisor(no_pelajar, penyelia):
    conn = create_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS penyelia_akademik (
            no_pelajar TEXT PRIMARY KEY,
            penyelia TEXT
        )
    """)
    c.execute("""
        INSERT OR REPLACE INTO penyelia_akademik (no_pelajar, penyelia)
        VALUES (?, ?)
    """, (no_pelajar, penyelia))
    conn.commit()
    conn.close()

def check_upload(no_pelajar, table):
    path = f"uploads/{table}/{table.upper()}_{no_pelajar}.pdf"
    return "✔️" if os.path.exists(path) else "❌"

st.header("🛠️ Panel Penyelaras Program")

program_code = st.selectbox("Pilih Program Anda", ["CS241", "CS248", "CS249", "CS290"])
admin_pass = st.text_input("Kata Laluan Penyelaras", type="password")

if admin_pass == "penyelaras2025":  # kata laluan contoh
    pelajar_list = get_students_by_program(program_code)

    if pelajar_list:
        for no_pelajar, nama, program in pelajar_list:
            st.markdown(f"### {nama} ({no_pelajar}) - {program}")
            penyelia = st.text_input(f"Nama Penyelia Akademik [{no_pelajar}]", key=no_pelajar)
            if st.button(f"Simpan Penyelia [{no_pelajar}]"):
                update_supervisor(no_pelajar, penyelia)
                st.success("Penyelia disimpan.")

            st.write("**Status Dokumen:**")
            st.markdown(f"- BLI-02: {check_upload(no_pelajar, 'bli_02')}")
            st.markdown(f"- Laporan Akhir: {check_upload(no_pelajar, 'laporan_akhir')}")

    else:
        st.info("Tiada pelajar dijumpai untuk program ini.")
else:
    st.warning("Masukkan kata laluan untuk akses.")
