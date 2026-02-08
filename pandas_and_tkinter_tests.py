import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import tkinter as tk

print ("hello !")

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
print(data["Code académie"].value_counts())
print("=============================================")
print(data["Code académie"].value_counts().plot.bar())
print("=============================================")
print(data.groupby("Genre").mean(numeric_only=True))
print("=============================================")
y = data["Code académie"]
x = data["Taux de réussite à l'examen"]
fig = plt.figure(figsize=(20,100))
plt.plot(x,y)
plt.title ("Graphique stylé")
plt.xlabel ("Taux de réussite à l'examen")
plt.ylabel ("Code académie")
# plt.plot( data["Nombre de présents à l'examen"], data["Code académie"], ) peut servir pour comparer deux colonnes
sns.barplot(data=data, x='Code département', y="Taux de réussite à l'examen", hue='Genre')
plt.title('diagramme session code académie et genre')
root = tk.Tk()
root.title("Histogramme du taux de réussite à l'examen par académie")
root.geometry("600x400")

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(data["Taux de réussite à l'examen"], bins=5, color="skyblue", edgecolor="black")

ax.set_title("Histogramme")
ax.set_xlabel("Code académie")
ax.set_ylabel("Taux de réussite à l'examen")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
plt.show ()
