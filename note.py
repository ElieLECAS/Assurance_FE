effectifs = data["quart_mois"].value_counts()
modalites = effectifs.index # l'index de effectifs contient les modalités

tab = pd.DataFrame(modalites, columns = ["quart_mois"]) # création du tableau à partir des modalités
tab["n"] = effectifs.values
tab["f"] = tab["n"] / len(data) # len(data) renvoie la taille de l'échantillon

tab = tab.sort_values("quart_mois") # tri des valeurs de la variable X (croissant)
tab["F"] = tab["f"].cumsum() # cumsum calcule la somme cumuléedata.loc[data['email'].duplicated(keep=False),:]



En Python, le calcul du mode tient en une ligne. Voici un exemple avec la variable montant :

data['montant'].mode()

Voici comment calculer la moyenne des montants dépensés :

data['montant'].mean()

Pour calculer la variance en Python, cela se fait très facilement ! Il suffit d'utiliser la méthode .var() sur la variable considérée. Par exemple avec la variable montant de notre jeu de données de transactions bancaires :

data['montant'].var()
Voici comment calculer la variance empirique corrigée en Python :

data['montant'].var(ddof=0)
Voilà comment calculer l'écart-type de la variable montant :

data['montant'].std()

Le calcul de ce dernier en Python est tout aussi simple :

data['montant'].std()/data['montant'].mean()
Nous pouvons facilement construire une boîte à moustaches avec Python :

data.boxplot(column="montant", vert=False)

plt.show()Le calcul du skewness se fait très facilement en Python. Voici un exemple avec la variable montant de notre jeu de données de transactions bancaires :

data['montant'].skew()Voilà comment calculer le kurtosis de notre variable montant :

data['montant'].kurtosis()

Nettoyer des données en Python est une étape cruciale dans le processus de prétraitement des données. Cela implique généralement la manipulation et la transformation des données pour les rendre utilisables dans des analyses ultérieures ou des modèles d'apprentissage automatique. Voici une explication détaillée des étapes générales pour nettoyer des données en Python :
1. Importer les bibliothèques nécessaires :

python

import pandas as pd
import numpy as np

Assurez-vous d'avoir installé ces bibliothèques à l'aide de la commande :

bash

pip install pandas numpy

2. Charger les données :

Si vos données sont stockées dans un fichier CSV, Excel, ou un autre format, utilisez les fonctions appropriées pour charger les données dans un DataFrame pandas.

python

# Exemple pour charger un fichier CSV
df = pd.read_csv('chemin_vers_le_fichier.csv')
# Afficher les premières lignes du DataFrame
print(df.head())

# Informations générales sur les données
print(df.info())

# Statistiques descriptives
print(df.describe())

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Supprimer les lignes avec des valeurs manquantes
df = df.dropna()

# Remplacer les valeurs manquantes par la moyenne
df['colonne'] = df['colonne'].fillna(df['colonne'].mean())

5. Gestion des valeurs aberrantes :

Identifiez et gérez les valeurs aberrantes qui peuvent fausser vos analyses.

python

# Identifier les valeurs aberrantes dans une colonne
Q1 = df['colonne'].quantile(0.25)
Q3 = df['colonne'].quantile(0.75)
IQR = Q3 - Q1
outliers = ((df['colonne'] < (Q1 - 1.5 * IQR)) | (df['colonne'] > (Q3 + 1.5 * IQR)))

# Supprimer les lignes avec des valeurs aberrantes
df = df[~outliers]

Nettoyer des données en Python est une étape cruciale dans le processus de prétraitement des données. Cela implique généralement la manipulation et la transformation des données pour les rendre utilisables dans des analyses ultérieures ou des modèles d'apprentissage automatique. Voici une explication détaillée des étapes générales pour nettoyer des données en Python :
1. Importer les bibliothèques nécessaires :

python

import pandas as pd
import numpy as np

Assurez-vous d'avoir installé ces bibliothèques à l'aide de la commande :

bash

pip install pandas numpy

2. Charger les données :

Si vos données sont stockées dans un fichier CSV, Excel, ou un autre format, utilisez les fonctions appropriées pour charger les données dans un DataFrame pandas.

python

# Exemple pour charger un fichier CSV
df = pd.read_csv('chemin_vers_le_fichier.csv')

3. Explorer les données :

Explorez vos données pour identifier les problèmes potentiels, tels que les valeurs manquantes, les valeurs aberrantes (outliers), les doublons, etc.

python

# Afficher les premières lignes du DataFrame
print(df.head())

# Informations générales sur les données
print(df.info())

# Statistiques descriptives
print(df.describe())

4. Traitement des valeurs manquantes :

Identifiez et gérez les valeurs manquantes. Vous pouvez les supprimer, les remplacer par une valeur spécifique ou utiliser des méthodes d'imputation plus avancées.

python

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Supprimer les lignes avec des valeurs manquantes
df = df.dropna()

# Remplacer les valeurs manquantes par la moyenne
df['colonne'] = df['colonne'].fillna(df['colonne'].mean())

5. Gestion des valeurs aberrantes :

Identifiez et gérez les valeurs aberrantes qui peuvent fausser vos analyses.

python

# Identifier les valeurs aberrantes dans une colonne
Q1 = df['colonne'].quantile(0.25)
Q3 = df['colonne'].quantile(0.75)
IQR = Q3 - Q1
outliers = ((df['colonne'] < (Q1 - 1.5 * IQR)) | (df['colonne'] > (Q3 + 1.5 * IQR)))

# Supprimer les lignes avec des valeurs aberrantes
df = df[~outliers]

6. Gestion des doublons :

Identifiez et supprimez les doublons éventuels dans les données.

python

# Identifier les doublons
duplicates = df.duplicated()

# Supprimer les lignes avec des doublons
df = df.drop_duplicates()
7. Transformation des types de données :

Assurez-vous que les types de données sont appropriés pour chaque colonne.

python

# Convertir une colonne en type datetime
df['date_col'] = pd.to_datetime(df['date_col'])

# Convertir une colonne en type catégorie
df['cat_col'] = df['cat_col'].astype('category')

8. Enregistrement des données nettoyées :

Enregistrez les données nettoyées dans un nouveau fichier si nécessaire.

python

df.to_csv('donnees_nettoyees.csv', index=False)