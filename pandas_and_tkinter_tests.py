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

#ca fait un histogramme sur le côté du taux de réussite à l'examen en fonction du genre. IMPORTANT !!
fig = plt.figure(figsize=(20,100))

plt.title ("Graphique stylé")
plt.xlabel ("Genre")
plt.ylabel ("Taux de réussite à l'examen")
# plt.plot( data["Nombre de présents à l'examen"], data["Code académie"], ) peut servir pour comparer deux colonnes
sns.barplot(data=data, x="Taux de réussite à l'examen", y="Genre")
plt.title("Diagramme du taux de réussite à l'examen en fonction du genre")

#ca fait un histogramme sur le côté du taux de réussite en fonction de la voie
fig = plt.figure(figsize=(20,100))

plt.title ("Graphique stylé")
plt.xlabel ("Voie")
plt.ylabel ("Taux de réussite à l'examen")
# plt.plot( data["Nombre de présents à l'examen"], data["Code académie"], ) peut servir pour comparer deux colonnes
sns.barplot(data=data, x="Taux de réussite à l'examen", y="Voie")
plt.title("Diagramme du taux de réussite à l'examen en fonction de la voie") 

#ca fait un histogramme du taux de réussite à l'examen en fonction du code département. IMPORTANT !!
root = tk.Tk()
root.title("Histogramme du taux de réussite à l'examen par code département")
root.geometry("1920x1080")

fig, ax = plt.subplots(figsize=(21, 10))
ax.hist(data["Code département"], bins=5, color="skyblue", edgecolor="black")

ax.set_title("Histogramme")
ax.set_xlabel("Code département")
ax.set_ylabel("Taux de réussite à l'examen")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
plt.show ()


root = tk.Tk()
root.title("Histogramme du taux de réussite à l'examen en fonction de la session")
root.geometry("1920x1080")

fig, ax = plt.subplots(figsize=(21, 10))
ax.hist(data["Session"], bins=5, color="skyblue", edgecolor="black")

ax.set_title("Histogramme")
ax.set_xlabel("Session")
ax.set_ylabel("Taux de réussite à l'examen")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
plt.show ()
