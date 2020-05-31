#!/usr/bin/env python3
import TableIt
from datetime import datetime
import sqlite3
def init_table():
    conn = sqlite3.connect("table.db")
    conn.cursor().execute("CREATE TABLE IF NOT EXISTS 'tasks' (date text, msg text)")
    conn.commit()
def add_entry_to_table(date, text):
    conn = sqlite3.connect("table.db")
    conn.cursor().execute(f"""INSERT INTO tasks VALUES('{date}', '{text}')
    """)
    conn.commit()

def get_entries() -> list:
    conn = sqlite3.connect("table.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM tasks""")
    s = cursor.fetchall()
    #print(s)
    s.insert(0,("ДАТА", "ТЕКСТ"))
    return s

def start_menu_selector() -> str:

    text = """
1) Прочитать задачи.
2) Добавить задачу."""
    print(text)
    resp = input("Ввод? => ")
    return resp

def main(keywords, table_name):
    try:
        resp = start_menu_selector()
        if resp == keywords["get_entries"]:
            queries = get_entries()
            TableIt.printTable(queries, useFieldNames=True)

        elif resp == keywords["add_entry_to_table"]:
            r = input("Введите заметку =>")
            add_entry_to_table(datetime.now(), r)
    except KeyboardInterrupt:
        print("Выходим...")
        exit(0)
    return
if __name__ == '__main__':
    keywords = {
        'get_entries': '1',
        'add_entry_to_table': '2',
    }
    table_name = "table.db"
    init_table()
    print("Для выхода нажми Ctrl-C")
    while True:
        main(keywords, table_name)
