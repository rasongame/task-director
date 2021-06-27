#!/usr/bin/env python3
import TableIt
import tkinter as tk
from datetime import datetime
from table_interact import *
class NewNoteFrame(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.master = parent
		self.pack()
		self.lbl = tk.Label(self, text="введи текст заметки")
		self.entry = tk.Entry(self)
		self.btn = tk.Button(self, text="добавить", command=self.add_note)
		self.lbl.pack(side="left")
		self.entry.pack(side="left")
		self.btn.pack(side="right")
	def add_note(self):
		nid = add_entry_to_table(datetime.now().strftime("%d %B %Y %I:%M%p"), self.entry.get())
		Note(self.master, self.entry.get(), datetime.now().strftime("%d %B %Y %I:%M%p"), nid)

class Note(tk.Frame):
	parent = None
	def __init__(self, parent, text, date, nid):
		super().__init__(parent)
		self.master = parent
		self.parent = parent
		self.pack()
		self.lbl = tk.Label(self, text=text)
		self.id = nid
		self.btn = tk.Button(self)
		self.btn["text"] = "удалить"
		self.btn['command'] = self.remove
		self.lbl.pack(side="left")
		self.btn.pack(side="right")
	def save(self):
		nid = add_entry_to_table(datetime.now().strftime("%d %B %Y %I:%M%p"), self.btn['text'])
		print(f'saved {nid}')
		self.id = nid

	def remove(self):
		remove_entry(self.id)
		self.destroy()

class App(tk.Frame):
	def __init__(self, master=None):
		self.tasks = list()
		super().__init__(master)
		self.db_file = "table.db"
		self.master = master
		self.pack()
		self.create_widgets()
	def load_tasks(self):
		tasks = get_entries()
		for task in tasks:
			note = Note(self, task[2], task[1], task[0])
			self.tasks.append(note)

	def create_widgets(self):
		self.load_tasks()
		NewNoteFrame(self)
		# self.hi_there = tk.Button(self)
		# self.hi_there["text"] = "Hello World\n(click me)"
		# self.hi_there["command"] = self.say_hi
		# self.hi_there.pack(side="top")

		self.quit = tk.Button(self, text="QUIT", fg="red",
							  command=self.master.destroy)
		self.quit.pack(side="bottom")

	def say_hi(self):
		print("hi there, everyone!")

root = tk.Tk()
app = App(master=root)
app.mainloop()

# def start_menu_selector() -> str:

#     text = """
# 1) Прочитать задачи.
# 2) Добавить задачу.
# 3) Удалить заметку."""
#     print(text)
#     resp = input("Ввод? => ")
#     return resp

# def main(keywords, table_name):
#     try:
#         resp = start_menu_selector()
#         if resp == keywords["get_entries"]:
#             queries = get_entries()
#             TableIt.printTable(queries, useFieldNames=True)

#         elif resp == keywords["add_entry_to_table"]:
#             r = input("Введите заметку =>")
#             add_entry_to_table(datetime.now().strftime("%d %B %Y %I:%M%p"), r)

#         elif resp == keywords["remove_entry"]:
#             r = input("Введите ИД заметки =>")
#             remove_entry(int(r))
#         else:
#             pass
#     except KeyboardInterrupt:
#         print("Выходим...")
#         exit(0)
#     return
# def drawLogo():
#     print("""   _            _          _ _               _
#  | |          | |        | (_)             | |
#  | |_ __ _ ___| | __   __| |_ _ __ ___  ___| |_ ___  _ __
#  | __/ _` / __| |/ /  / _` | | '__/ _ \/ __| __/ _ \| '__|
#  | || (_| \__ \   <  | (_| | | | |  __/ (__| || (_) | |
#   \__\__,_|___/_|\_\  \__,_|_|_|  \___|\___|\__\___/|_|

#                                                           """)
# if __name__ == '__main__':
#     keywords = {
#         'get_entries': '1',
#         'add_entry_to_table': '2',
#         'remove_entry': '3'
#     }
#     table_name = "table.db"
#     init_table()
#     drawLogo()
#     print("Для выхода нажми Ctrl-C")
#     while True:
#         main(keywords, table_name)
