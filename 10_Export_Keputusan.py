# pages/10_Export_Keputusan.py

import streamlit as st
import sqlite3
import pandas as pd

def create_connection():
    return sqlite3.connect("latihan_industri.db", check_same_thread=False)

def get_final_scores(program_code):
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        SELECT b.no_pelajar, b.nama, b.program,
               COALESCE(i.keseluruhan, 0) * 0.30 AS industri_score,
               COALESCE(a.skor_laporan, 0) * 1.0 AS laporan,
               COALESCE(a.skor_logbook, 0) * 1.0 AS logbook,
               COALESCE(a.skor_tambahan, 0) * 1.0 AS tambahan
        FROM bli01 b
        LEFT JOIN penilaian_industri i ON b.no_pelajar = i.no_pelajar
        LEFT JOIN penilaian_akademik a ON b.no_pelajar = a.no_pelajar
        WHERE b.program LIKE ?
    """, (f"%{program_code}%",))

    data = c.fetchall()
    conn.close()

    result = []
    for row in data:
        no_pelajar, nama, program, industri, laporan, logbook, tambahan = row
        akademik_total = laporan + logbook + tambahan
        total = industri + akademik_total
        result.append({
            "No. Pelajar": no_pelajar,
            "Nama": nama,
            "Program": program,
            "Markah Industri (30%)": round(industri, 2),
            "Markah Akademik (70%)": round(akademik_total, 2),
            "Jumlah Markah Akhir (100%)": round(total, 2)
        })
    return pd.DataFrame(result)

st.header("📥 Eksport Keputusan Akhir Pelajar")

program_code = st.selectbox("Pilih Program", ["CS241", "CS248", "CS249", "CS290"])
admin_pass = st.text_input("Kata Laluan Penyelaras", type="password")

if admin_pass == "penyelaras2025":
    df = get_final_scores(program_code)
    st.dataframe(df, use_container_width=True)

    if not df.empty:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📤 Muat Turun CSV Keputusan", data=csv, file_name=f"Keputusan_{program_code}.csv")
else:
    st.warning("Masukkan kata laluan untuk akses.")
