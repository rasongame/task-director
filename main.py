#!/usr/bin/env python3
import TableIt
import tkinter as tk
from datetime import datetime
from table_interact import *

class NewNoteFrame(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.is_multiline = False
		self.master = parent
		# self.pack(side="bottom")
		self.lbl = tk.Label(self, text="введи текст заметки")
		self.entry = tk.Entry(self)
		self.entry.bind("<Return>", self.add_note)
		self.entry.bind("<Delete>", parent.check_can_remove_selected)
		# bind for <Return> key
		self.grid(sticky=tk.N)
		self.btn = tk.Button(self, text="добавить", command=self.add_note)
		self.lbl.grid(row=1, column=1)
		self.entry.grid(row=1, column=2)
		self.btn.grid(row=1, column=3)
		# self.lbl.grid(side="left")
		# self.entry.grid(side="left")
		# self.btn.grid(side="right")

	def add_note(self, *args):
		nid = add_entry_to_table(datetime.now().strftime("%d %B %Y %I:%M%p"), self.entry.get())
		Note(self.master, self.entry.get(), datetime.now().strftime("%d %B %Y %I:%M%p"), nid)

class Note(tk.Frame):
	parent = None
	def __init__(self, parent, text, date, nid):
		super().__init__(parent)
		self.master = parent
		self.parent = parent
		self.grid()
		self.lbl = tk.Label(self, text=text, wraplength=1000)
		self.id = nid
		self.btn = tk.Button(self)
		self.btn["text"] = "удалить"
		self.btn['command'] = self.remove
		self.is_checked = tk.IntVar()
		self.chk = tk.Checkbutton(self, variable=self.is_checked)
		self.chk.grid(row=2, column=1)
		self.lbl.grid(row=2, column=2)
		self.btn.grid(row=2, column=3)

	def save(self):
		nid = add_entry_to_table(datetime.now().strftime("%d %B %Y %I:%M%p"), self.btn['text'])
		print(f'saved {nid}')
		self.id = nid

	def remove(self):
		remove_entry(self.id)
		self.destroy()

class App(tk.Frame):
	def check_can_remove_selected(self, *args):
		buttons = list(filter(lambda task: task.is_checked.get(), self.tasks))
		if len(buttons) > 1:
			[note.remove() for note in buttons]

	def __init__(self, master=None):
		self.tasks = list()
		super().__init__(master)
		self.db_file = "table.db"
		self.master = master
		self.create_widgets()
		
	def load_tasks(self):
		tasks = get_entries()
		for task in tasks:
			note = Note(self, task[2], task[1], task[0])
			self.tasks.append(note)

	def create_widgets(self):
		self.quit = tk.Button(self, text="QUIT", fg="red",
							  command=self.master.destroy)
		self.quit.grid()
		self.entry = NewNoteFrame(self)
		self.load_tasks()

		self.grid()
		# self.pack()

	def say_hi(self):
		print("hi there, everyone!")

root = tk.Tk()
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=3)
app = App(master=root)
app.mainloop()