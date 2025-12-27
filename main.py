from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tk()
root.title("Résultats du Baccalauréat par Département")
data = pd.read_excel('fr-en-baccalaureat-par-departement.xlsx')
my_label = Label (root, text = "Commencer" )
my_label.pack()
root.mainloop()
