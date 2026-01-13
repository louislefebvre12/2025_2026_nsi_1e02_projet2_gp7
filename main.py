from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tk()
root.title("Résultats du Baccalauréat par Département")
data = pd.read_excel('fr-en-baccalaureat-par-departement.xlsx')
photo = PhotoImage(file="cartedep.png")
window.minsize(height=window.winfo_height(), width=window.winfo_width())
button = Button(window, text=0, command=buttonclicked)
button.grid(column=1, row=1)
my_label = Label (root, text = "Commencer", image = photo)
my_label.pack()
root.mainloop()
