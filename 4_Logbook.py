# pages/4_Logbook.py

import streamlit as st
import sqlite3
import datetime

def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

def simpan_logbook(no_pelajar, minggu, aktiviti, tarikh):
    conn = create_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logbook (
            no_pelajar TEXT,
            minggu INTEGER,
            tarikh TEXT,
            aktiviti TEXT,
            PRIMARY KEY (no_pelajar, minggu)
        )
    """)
    c.execute("""
        INSERT OR REPLACE INTO logbook (no_pelajar, minggu, tarikh, aktiviti)
        VALUES (?, ?, ?, ?)
    """, (no_pelajar, minggu, tarikh, aktiviti))
    conn.commit()
    conn.close()

def lihat_logbook(no_pelajar):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT minggu, tarikh, aktiviti FROM logbook WHERE no_pelajar=? ORDER BY minggu", (no_pelajar,))
    results = c.fetchall()
    conn.close()
    return results

st.header("📘 Logbook Latihan Industri")

if "pelajar" in st.session_state:
    no_pelajar = st.session_state["pelajar"][2]
    minggu = st.number_input("Minggu ke-", min_value=1, max_value=20, step=1)
    tarikh = st.date_input("Tarikh", datetime.date.today())
    aktiviti = st.text_area("Catatan Aktiviti Mingguan")

    if st.button("Hantar Logbook"):
        simpan_logbook(no_pelajar, minggu, str(tarikh), aktiviti)
        st.success(f"Logbook minggu ke-{minggu} telah dihantar.")

    st.subheader("📄 Logbook Terdahulu")
    for m, t, a in lihat_logbook(no_pelajar):
        st.markdown(f"**Minggu {m}** ({t}):

{a}
---")
else:
    st.warning("Sila log masuk terlebih dahulu.")
