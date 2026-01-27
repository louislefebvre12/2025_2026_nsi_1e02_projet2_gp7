from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def plot() : 
    ax.clear()

    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    ax.scatter(x,y)
    canvas.draw() 


root = Tk()
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master = root)

frame = Frame(root)
label = Label(text = ' Résultats au BAC', padx = 10, pady = 10, borderwidth = 2, relief = 'solid')
label.config(font=("Courrier", 32))
label.pack()

for i in range(1, 6):
    Button(
        frame,
        text=f'Statistiques {i}',
        command=plot
    ).pack(side=LEFT, padx=10, pady=10)

canvas.get_tk_widget().pack()

frame.pack()

root.mainloop()
