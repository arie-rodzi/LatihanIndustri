# pages/1_Login_Pelajar.py

import streamlit as st
import sqlite3

# Fungsi sambungan ke database
def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

# Fungsi login
def login(no_pelajar, katalaluan):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM pelajar WHERE no_pelajar=? AND katalaluan=?", (no_pelajar, katalaluan))
    result = c.fetchone()
    conn.close()
    return result

# UI login
st.header("🔐 Log Masuk Pelajar")
no_pelajar = st.text_input("No. Pelajar")
katalaluan = st.text_input("Kata Laluan", type="password")

if st.button("Log Masuk"):
    user = login(no_pelajar, katalaluan)
    if user:
        st.success(f"Selamat datang, {user[1]}!")
        st.session_state["pelajar"] = user
    else:
        st.error("Maklumat tidak sah. Sila cuba lagi.")
