import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window1:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Fenêtre 1")
        ttk.Label(self.window, text="Contenu fenêtre 1").pack(padx=40, pady=40)
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




