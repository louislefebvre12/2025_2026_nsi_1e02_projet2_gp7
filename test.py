import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('fr-en-baccalaureat-par-departement.xlsx')
print(data)
print("=============================================")
# data = pd.DataFrame(data)
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
# plt.plot( data["Nombre de présents à l'examen"], data["Code académie"], ) peut servir pour comparer deux colonnes
plt.show ()