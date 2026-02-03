import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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
y = data["Genre"]
x = data["Taux de réussite à l'examen"]
fig = plt.figure(figsize=(20,100))
plt.plot(x,y)
plt.title ("Test")
plt.xlabel ("Axe x")
plt.ylabel ("Axe y")
# plt.plot( data["Nombre de présents à l'examen"], data["Code académie"], ) peut servir pour comparer deux colonnes
data.plot(x='x', y='y')
plt.show ()