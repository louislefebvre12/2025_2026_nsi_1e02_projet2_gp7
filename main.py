from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


data_A = {'x': [1, 2, 3, 4, 5], 'y': [1, 4, 9, 16, 25]}
data_B = {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1]} 
data_C = {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5]} 
data_D = {'x': [1, 2, 3, 4, 5], 'y': [5, 10, 15, 20, 25]}  


dfs = {
    'A': pd.DataFrame(data_A),
    'B': pd.DataFrame(data_B),
    'C': pd.DataFrame(data_C),
    'D': pd.DataFrame(data_D)
}


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
