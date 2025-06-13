# utils/database.py

import sqlite3

# Cipta jadual pelajar
def init_db():
    conn = sqlite3.connect("latihan_industri.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pelajar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            no_pelajar TEXT UNIQUE,
            katalaluan TEXT,
            program TEXT,
            emel TEXT
        )
    """)
    conn.commit()
    conn.close()

# Masukkan pelajar (untuk ujian)
def add_sample_pelajar():
    conn = sqlite3.connect("latihan_industri.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO pelajar (nama, no_pelajar, katalaluan, program, emel) VALUES (?, ?, ?, ?, ?)", 
                  ("Ali Bin Ahmad", "2023123456", "abc123", "CS241", "ali@student.uitm.edu.my"))
    except sqlite3.IntegrityError:
        pass  # skip if already exists
    conn.commit()
    conn.close()

# Panggil fungsi semasa import
init_db()
add_sample_pelajar()
