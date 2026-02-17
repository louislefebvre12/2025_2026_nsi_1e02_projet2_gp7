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

#ca fait un histogramme sur le côté du taux de réussite à l'examen en fonction du genre. IMPORTANT !!
fig = plt.figure(figsize=(20,100))

plt.title ("Graphique stylé")
plt.xlabel ("Genre")
plt.ylabel ("Taux de réussite à l'examen")
# plt.plot( data["Nombre de présents à l'examen"], data["Code académie"], ) peut servir pour comparer deux colonnes
sns.barplot(data=data, x="Taux de réussite à l'examen", y="Genre")
plt.title("Diagramme du taux de réussite à l'examen en fonction du genre")
plt.plot()
plt.show ()

#ca fait un histogramme sur le du taux de réussite en fonction de la voie
fig = plt.figure(figsize=(20,100))

plt.title ("Graphique stylé")
plt.xlabel ("Voie")
plt.ylabel ("Taux de réussite à l'examen")
# plt.plot( data["Nombre de présents à l'examen"], data["Code académie"], ) peut servir pour comparer deux colonnes
sns.barplot(data=data, x="Taux de réussite à l'examen", y="Voie")
plt.title("Diagramme du taux de réussite à l'examen en fonction de la voie") 
plt.show ()

#ca fait un histogramme du taux de réussite à l'examen en fonction du code département. IMPORTANT !!
root = tk.Tk()
root.title("Histogramme du taux de réussite à l'examen par code département")
root.geometry("1920x1080")

fig, ax = plt.subplots(figsize=(21, 10))
ax.hist(data["Code département"], bins=5, color="darkmagenta", edgecolor="black")

ax.set_title("Histogramme")
ax.set_xlabel("Code département")
ax.set_ylabel("Taux de réussite à l'examen")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
plt.show ()


#ca fait un camembew du taux de réussite par voie

colonne_categorie = "Voie"
colonne_valeur = "Taux de réussite à l'examen"

root = tk.Tk()
root.title("Camembert du taux de réussite à l'examen par voie")
root.geometry("1920x1080")

fig = plt.Figure(figsize=(10, 10))
ax = fig.add_subplot(111)

df_grouped = data.groupby(colonne_categorie)[colonne_valeur].mean()

wedges, texts, autotexts = ax.pie(
    df_grouped.values,
    labels=df_grouped.index,
    autopct="%1.1f%%",
    startangle=90
)

ax.legend(
    wedges,                   # les parts du camembew
    df_grouped.index,         # noms des catégories
    title="Voie",
    loc="center right",        # position de la légende
    bbox_to_anchor=(1, 0, 0.5, 1)  # décalage pour qu'elle ne chevauche pas le graphique
)
ax.legend(
    wedges,
    df_grouped.index,
    title="Taux de réussite à l'examen",
    loc="center right",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

ax.set_title("Taux de réussite moyen par voie")
ax.axis("equal")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()