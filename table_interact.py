#!/usr/bin/env python3
import sqlite3
def get_entries() -> list:
    conn = sqlite3.connect("table.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT rowid, * FROM tasks""")
    s = cursor.fetchall()
    #print(s)
    s.insert(0,("ИД", "ДАТА", "ТЕКСТ"))
    return s
def init_table():
    conn = sqlite3.connect("table.db")
    conn.cursor().execute("CREATE TABLE IF NOT EXISTS 'tasks' (date text, msg text)")
    conn.commit()
def remove_entry(row_id):
    conn = sqlite3.connect('table.db')
    conn.cursor().execute(f"DELETE from tasks where rowid={row_id}")
    conn.commit()
def add_entry_to_table(date, text):
    conn = sqlite3.connect("table.db")
    conn.cursor().execute(f"""INSERT INTO tasks VALUES('{date}', '{text}')
    """)
    conn.commit()
