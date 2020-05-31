#!/usr/bin/env python3
import TableIt
from datetime import datetime
from table_interact import *




def start_menu_selector() -> str:

    text = """
1) Прочитать задачи.
2) Добавить задачу.
3) Удалить заметку."""
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
            add_entry_to_table(datetime.now().strftime("%d %B %Y %I:%M%p"), r)

        elif resp == keywords["remove_entry"]:
            r = input("Введите ИД заметки =>")
            remove_entry(int(r))
        else:
            pass
    except KeyboardInterrupt:
        print("Выходим...")
        exit(0)
    return
def drawLogo():
    print("""   _            _          _ _               _
 | |          | |        | (_)             | |
 | |_ __ _ ___| | __   __| |_ _ __ ___  ___| |_ ___  _ __
 | __/ _` / __| |/ /  / _` | | '__/ _ \/ __| __/ _ \| '__|
 | || (_| \__ \   <  | (_| | | | |  __/ (__| || (_) | |
  \__\__,_|___/_|\_\  \__,_|_|_|  \___|\___|\__\___/|_|

                                                          """)
if __name__ == '__main__':
    keywords = {
        'get_entries': '1',
        'add_entry_to_table': '2',
        'remove_entry': '3'
    }
    table_name = "table.db"
    init_table()
    drawLogo()
    print("Для выхода нажми Ctrl-C")
    while True:
        main(keywords, table_name)
