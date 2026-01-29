
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





