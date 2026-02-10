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
print(data["Code académie"].value_counts().plot.bar())
print("=============================================")
print(data.groupby("Genre").mean(numeric_only=True))
print("=============================================")
#Diagramme de dispersion a corriger
y = data["Code académie"]
x = data["Genre"]
fig = plt.figure(figsize=(20,100))
plt.scatter(x,y)
plt.title ("Test")
plt.xlabel ("Axe x")
plt.ylabel ("Axe y")
plt.plot( data["Genre"], data["Code académie"], ) #peut servir pour comparer deux colonnes
print("=============================================")
#Tracé linéaire a corriger
aggregation_trace = "mean"
data = pd.read_excel("fr-en-baccalaureat-par-departement.xlsx")
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
data["Taux de réussite à l'examen"] = pd.to_numeric(data["Taux de réussite à l'examen"], errors='coerce')
if aggregation_trace == "mean":
    df = data.groupby("Code académie", as_index=False)["Taux de réussite à l'examen"].mean()
else:
    raise ValueError("Probleme de donnés")
df = df.sort_values("Code académie")
root = tk.Tk()
root.title("Courbe du taux de réussite par académie")
root.geometry("1200x800")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(
    data=df,
    x="Code académie",
    y="Taux de réussite à l'examen",
    marker="o",
    ax=ax
)
ax.set_title("Courbe du taux de réussitepar académie")
ax.set_xlabel("Code académie")
ax.set_ylabel("Taux de réussite à l'examen à l'examen")
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=root)
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

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
print("=============================================")
#Camembert a corriger
aggregation_camembert = "sum" 
TITLE = "Répartition par genre"
data = pd.read_excel("fr-en-baccalaureat-par-departement.xlsx")
data.columns = data.columns.str.strip()
if aggregation_camembert == "sum":
    df = data.groupby("Genre", as_index=False)["Session"].sum()
else:
    raise ValueError("Probleme de donnés")
root = tk.Tk()
root.title("Répartition par genre")
root.geometry("900x700")
fig, ax = plt.subplots(figsize=(12, 12))
ax.pie(
    df["Session"],
    labels=df["Genre"],
    autopct='%1.1f%%',
    startangle=90
)
ax.set_title("Répartition par genre")
ax.axis('equal')  # cercle parfait
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
print("=============================================")
#Diagramme à barres groupées a corriger
#sns.barplot(data=data, x='Voie', y='Session', hue='Genre')
#plt.title('diagramme session voie et genre')
plt.show ()