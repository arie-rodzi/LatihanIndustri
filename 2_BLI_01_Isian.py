# pages/2_BLI_01_Isian.py

import streamlit as st
import sqlite3

def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

def simpan_bli01(no_pelajar, data):
    conn = create_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS bli01 (
            no_pelajar TEXT PRIMARY KEY,
            nama TEXT,
            nokp TEXT,
            program TEXT,
            bahagian TEXT,
            cgpa TEXT,
            telefon TEXT,
            emel TEXT,
            alamat TEXT,
            telefon_penjaga TEXT
        )
    """)
    c.execute("""
        INSERT OR REPLACE INTO bli01 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (no_pelajar, *data))
    conn.commit()
    conn.close()

st.header("📄 BLI-01: Borang Maklumat Peribadi")

if "pelajar" in st.session_state:
    user = st.session_state["pelajar"]
    no_pelajar = user[2]

    nama = st.text_input("Nama", user[1])
    nokp = st.text_input("No. KP")
    program = st.text_input("Program", user[4])
    bahagian = st.text_input("Bahagian")
    cgpa = st.text_input("CGPA")
    telefon = st.text_input("No. Telefon Bimbit")
    emel = st.text_input("Alamat E-mel", user[5])
    alamat = st.text_area("Alamat Surat-Menyurat")
    telefon_penjaga = st.text_input("No. Telefon (Penjaga)")

    if st.button("Hantar BLI-01"):
        data = (nama, nokp, program, bahagian, cgpa, telefon, emel, alamat, telefon_penjaga)
        simpan_bli01(no_pelajar, data)
        st.success("Borang BLI-01 berjaya dihantar dan disimpan.")
else:
    st.warning("Sila log masuk terlebih dahulu.")
