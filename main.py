
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Extra(Toplevel):
	def __init__(self):
		super().__init__()
		self.title('extra window')
		self.geometry('300x400')
		Label(self, text = 'A label').pack()
		Button(self, text = 'A button').pack()
		Label(self, text = 'another label').pack(expand = True)
		self.plot_window ()
	
	def plot_window(self):
<<<<<<< Updated upstream
		top = Toplevel(self)
		top.title("Résultats au BAC")
		top.geometry("900x600")

		fig, ax = plt.subplots(figsize=(6, 4))
		canvas = FigureCanvasTkAgg(fig, master=top)

		label = Label(
			top,
			text='Résultats au BAC',
			padx=10,
			pady=10,
			borderwidth=2,
			relief='solid',
			font=("Courier", 24)
		)
		label.pack(pady=10)

		frame = Frame(top)
		frame.pack(pady=10)

		for i in range(1, 7):
			Button(
				frame,
				text=f'Statistiques {i}',
				command=lambda i=i: print(f"Stat {i}")
			).pack(side=LEFT, padx=5)

		canvas.get_tk_widget().pack(expand=True, fill=BOTH)
=======
		root = Tk()
		fig, ax = plt.subplots()
		canvas = FigureCanvasTkAgg(fig, master = root)
		frame = Frame(root)
		label = Label(text = ' Résultats au BAC', padx = 10, pady = 10, borderwidth = 2, relief = 'solid')
		label.config(font=("Courrier", 32))
		label.pack()
		Button(frame,text=f'Statistiques 1',command=plt).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 2',command=plt).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 3',command=plt).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 4',command=plt).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 5',command=plt).pack(side=LEFT, padx=10, pady=10)
		Button(frame,text=f'Statistiques 6',command=plt).pack(side=LEFT, padx=10, pady=10)
		canvas.get_tk_widget().pack()
		frame.pack()
		root.mainloop()

listbox = Tk.Listbox(root)
for col in df.columns:
    listbox.insert(tk.END, col)
listbox.pack()

def valider():
    selection = listbox.get(listbox.curselection())
    print(selection)
>>>>>>> Stashed changes
	



def ask_yes_no():
	messagebox.showerror('Info title', 'Here is some information')


	

def close_window():
	exit()


window = Tk()
window.geometry('600x400')
window.title('Multiple windows')


button1 = Button(window, text = 'Open main window', command = plot_window(self))
button1.pack(expand = True)

button2 = Button(window, text = 'Close main window', command = close_window)
button2.pack(expand = True)

button3 = Button(window, text = 'create yes no window', command = ask_yes_no)
button3.pack(expand = True)

window.mainloop()





