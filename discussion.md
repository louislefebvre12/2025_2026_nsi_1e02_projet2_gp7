faut installer python  sur le pc abev ce lien https://www.python.org/downloads/

fonctions pandas:

df.head()   afficher le début du dataframe
df.describe()   statistiques rapides 
df.drop(['column','column',...]) éliminer certaines colonnes 
df.dropna(axis=0) éliminer les lignes aux données manquantes
df.['column'].value_counts() compter les répétitions 
df.groupby(['column']) analyse par groupe
data = data.drop(['column','column',...], axis=1) éliminer des colonnes
data.shape afficher les limites du dossier
data.columns afficher les colonnes du dossier avec les titres
data.head() afficher les premieres lignes du dossier