import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import tkinter as tk


data = pd.read_excel('fr-en-baccalaureat-par-departement.xlsx')
print(data)
print("=============================================")
data = pd.DataFrame(data)
print(data.shape)
print("=============================================")
print(data.columns)
print("=============================================")
print(data.head())
print("=============================================")
print(data.describe())
print("=============================================")

#ca fait un graphique camembert du taux de réussite entre les voies

colonne_categorie = "Voie"
colonne_valeur = "Taux de réussite à l'examen"

root = tk.Tk()
root.title("Camembert du taux de réussite à l'examen par voie")
root.geometry("1920x1080")

fig = plt.Figure(figsize=(10, 10))
ax = fig.add_subplot(111)

df_grouped = data.groupby(colonne_categorie)[colonne_valeur].mean()

ax.pie(
    df_grouped.values,
    labels=df_grouped.index,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Taux de réussite moyen par voie")
ax.axis("equal")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()