
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from model import Model
from view import View

class Controller:
    def __init__(self, root, model, view):
       
        self.model = model
        self.view = view

        self.view.self.button1.config(command=self.close_window)
        self.view.self.button2.config(command=self.close_window)
        self.view.self.button3.config(command=self.close_window)
        self.view.self.button4.config(command=self.close_window)
        
        def close_window() :
            view.destroy()
        
        def prediction_window ():
            pass

        def ranking_window() : 
            pass

        def plot_window() : 
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

