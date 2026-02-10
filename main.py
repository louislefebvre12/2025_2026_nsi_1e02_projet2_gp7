
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Extra(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('extra window')
        self.geometry('300x400')

        Label(self, text='A label').pack()
        Button(self, text='A button').pack()
        Label(self, text='another label').pack()

        self.plot_window()

    def plot_window(self):
        top = Toplevel(self)
        top.title("Résultats au BAC")
        top.geometry("900x600")

        fig, ax = plt.subplots(figsize=(6, 4))
        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=BOTH)

def ask_yes_no():
    messagebox.showerror('Info title', 'Here is some information')

window = Tk()
Extra(window)
window.mainloop()






