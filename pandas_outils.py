import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
#code_academie_genre = data[['Voie', 'Genre']].astype({'Voie': 'string'}).groupby('Genre').sum().reset_index()
#plt.plot(code_academie_genre['Voie'], code_academie_genre['Genre'])
#plt.title('Code académie par genre')
print("=============================================")
#Histogramme a corriger
#plt.hist(data['Genre'])
#plt.title('Histogramme genre')
print("=============================================")
#Camembert a corriger
#data = data('')['Genre'].count().reset_index()
#plt.pie(data['Genre'], labels=data['Code académie'])
#plt.title('Camembert code académie et genre')
print("=============================================")
#Diagramme à barres groupées a corriger
#sns.barplot(data=data, x='Voie', y='Session', hue='Genre')
#plt.title('diagramme session voie et genre')
plt.show ()