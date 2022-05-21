import sqlite3 as sq

with sq.connect('PZ_16/patient.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pat_fio TEXT NOT NULL,
        doc_fio TEXT NOT NULL,
        diagnosis TEXT NOT NULL,
        cost INTEGER
    )""")
