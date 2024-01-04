import pandas as pd

dataset_path = "C:\Users\33679\OneDrive\Bureau\Nouveau dossier (3)\Projet assurance\Assurance_FE\Dataset_Brief.csv"
df = pd.read_csv(dataset_path)

# Informations générales sur les données
print(df.info())

print("Avant nettoyage:")
print(df.head())

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Supprimer les lignes avec des valeurs manquantes
# df = df.dropna()

# Remplacer les valeurs manquantes par la moyenne
# df['colonne'] = df['colonne'].fillna(df['colonne'].mean())

#duplicates
duplicates = df.duplicated(subset=["age", "sex", "bmi", "children", "smoker", "region"])
duplicates_data = df[duplicates]
#
print("\nLignes avec des duplicatas:")
print(duplicates_data)
#
df = df.drop_duplicates(subset=["age", "sex", "bmi", "children", "smoker", "region"], keep='first')
#
print("\nAprès vérification de duplicatas:")
print(df.head())
#

df['age'] = df['age'].astype(int)