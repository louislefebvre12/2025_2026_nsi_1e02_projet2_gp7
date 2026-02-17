import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
#Graphique baton
print(data["Code académie"].value_counts().plot.bar())
print("=============================================")
print(data.groupby("Genre").mean(numeric_only=True))
print("=============================================")
#Diagramme de dispersion 
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=data,
    x="Nombre de présents à l'examen",
    y="Nombre d'admis à l'examen",
    hue="Voie" #couleur
)

plt.title("Présents vs Admis (par voie)")
plt.tight_layout()

print("=============================================")
#Tracé linéaire 
aggregation_trace = "mean" #prend la moyenne
data = pd.read_excel("fr-en-baccalaureat-par-departement.xlsx") #fichier

data.columns = (
    data.columns
    .str.strip()
)

data["Taux de réussite à l'examen"] = (
    data["Taux de réussite à l'examen"]
    .astype(str)
    .str.replace('%', '', regex=False)
    .str.replace(',', '.', regex=False)
)

data["Taux de réussite à l'examen"] = pd.to_numeric(data["Taux de réussite à l'examen"], errors='coerce') #prend le taux de réussite pour le rendre utilisable

if aggregation_trace == "mean": #vérifie que c bien une moyenne pour l'aggregation du tracé et sinon met un message d'erreur
    df = data.groupby("Code académie", as_index=False)["Taux de réussite à l'examen"].mean()
else:
    raise ValueError("Probleme de donnés")

df = df.sort_values("Code académie")
root = tk.Tk()
root.title("Courbe du taux de réussite par académie")
root.geometry("1200x800")
fig, ax = plt.subplots(figsize=(10, 6))

sns.lineplot( #seaborn pour le tracé avec les deux axes x et y
    data=df,
    x="Code académie",
    y="Taux de réussite à l'examen",
    marker="o",
    ax=ax
)

ax.set_title("Tracé du taux de réussite par académie")
ax.set_xlabel("Code académie")
ax.set_ylabel("Taux de réussite à l'examen à l'examen")
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=root) #affichage
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
print("=============================================")
#Histogramme a corriger
root = tk.Tk()
root.title("Histogramme du Taux de réussite à l'examen à l'examen par genre")
root.geometry("1920x1080")

fig, ax = plt.subplots(figsize=(16, 9))
ax.hist(data["Genre"], bins=5, color="skyblue", edgecolor="black")

ax.set_title("Histogramme")
ax.set_xlabel("Genre")
ax.set_ylabel("Taux de réussite à l'examen à l'examen")

ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
print("=============================================")
#Camembert a corriger
aggregation_camembert = "sum" #prend la somme

data = pd.read_excel("fr-en-baccalaureat-par-departement.xlsx")
data.columns = data.columns.str.strip()

if aggregation_camembert == "sum": #aggrégation vérifie que c une somme sinon message d'erreur
    df = data.groupby(["Genre", "Voie"], as_index=False)["Session"].sum()
else:
    raise ValueError("Problème de données")

df["Label"] = df["Genre"] + " - " + df["Voie"] #pppour un meilleur affichage divise les 3 vois par les 2 genres

root = tk.Tk()
root.title("Répartition par genre et voie")
root.geometry("1200x800")

fig, ax = plt.subplots(figsize=(12, 12))

ax.pie( #permet de créer le camembert
    df["Session"],
    labels=df["Label"],
    autopct='%1.1f%%',
    startangle=90
)

ax.set_title("Répartition par genre et voie")
ax.axis('equal')  # cercle parfait
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root) #affichage
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
print("=============================================")
#Diagramme à barres groupées a corriger
#sns.barplot(data=data, x='Voie', y='Session', hue='Genre')
#plt.title('diagramme session voie et genre')

#Diagrammes à barres
differents_taux_groupes = data[['Département', 'Taux de réussite']].groupby('Département').mean().reset_index()


plt.bar(data['Département'], differents_taux_groupes['bill_length_mm'])
plt.title('PPLus haut taux de réussite par département')


plt.show ()