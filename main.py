import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Extra(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.title('extra window')
		self.geometry('300x400')
		ttk.Label(self, text = 'A label').pack()
		ttk.Button(self, text = 'A button').pack()
		ttk.Label(self, text = 'another label').pack(expand = True)
		self.plot_window ()
	def plot_window(self):
		root = Tk()
		fig, ax = plt.subplots()
		canvas = FigureCanvasTkAgg(fig, master = root)
		frame = Frame(root)
		label = Label(text = ' Résultats au BAC', padx = 10, pady = 10, borderwidth = 2, relief = 'solid')
		label.config(font=("Courrier", 32))
		label.pack()
		Button(frame,text=f'Statistiques 1',command=plot).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 2',command=plot).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 3',command=plot).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 4',command=plot).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 5',command=plot).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 6',command=plot).pack(side=LEFT, padx=10, pady=10)
		canvas.get_tk_widget().pack()
		frame.pack()
		root.mainloop()
	

# https://docs.python.org/3/library/tkinter.messagebox.html
def ask_yes_no():
	# answer = messagebox.askquestion('Title', 'Body')
	# print(answer)
	messagebox.showerror('Info title', 'Here is some information')

def create_window():
	global extra_window
	extra_window = Extra()
	

def close_window():
	extra_window.destroy()

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

button1 = ttk.Button(window, text = 'open main window', command = create_window)
button1.pack(expand = True)

button2 = ttk.Button(window, text = 'close main window', command = close_window)
button2.pack(expand = True)

button3 = ttk.Button(window, text = 'create yes no window', command = ask_yes_no)
button3.pack(expand = True)

# run 
window.mainloop()