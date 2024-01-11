import streamlit as st 
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime, timedelta


def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def page_prediction():
    st.title("Assur'ément - Saisie de Données pour la Prédiction")

    st.write(
        "Utilisez cette page pour entrer les données nécessaires à la prédiction du prix de l'assurance."
    )

    birthdate = st.date_input("Veuillez sélectionner votre date de naissance.", format="DD/MM/YYYY")
    min_age_required = 18
    if birthdate:
        age = calculate_age(birthdate)
        if age < min_age_required:
            st.error(f"Vous devez avoir au moins {min_age_required} ans pour utiliser cette application.")
        else:
            st.write(f"Âge actuel : {age} ans")

    sex = st.radio("Sexe", ["Homme", "Femme"])

    smoker = st.checkbox("Êtes-vous Fumeur", False)
    st.write(f"Vous êtes {'fumeur' if smoker else 'non_fumeur'}")

    poids = st.number_input("Entrez votre Poids (kg)", min_value=0.00, max_value=150.00, value=70.00)
    st.write(f"Votre poids est {poids} kg")

    taille = st.number_input("Entrez votre Taille (cm)", min_value=0.00, max_value=220.00, value=170.00)
    st.write(f"Votre taille est {taille/100} m")

    bmi = round(poids / (taille / 100)**2, 2)
    st.write(f"Votre IMC est de {bmi}")

    children = st.number_input("Entrez le nombre(s) d'enfant(s)", min_value=0, value=0)
    if children == 1:
        st.write(f"Vous avez {children} enfant")
    elif children == 0:
        st.write(f"Vous n'avez pas d'enfants")
    else:
        st.write(f"Vous avez {children} enfants")

    region = st.selectbox("Sélectionnez une région", ["northwest", "northeast", "southwest", "southeast"])
    st.write(f"Vous habitez au {region}")

    if sex == 'Homme':
        sex = 0
    else:
        sex = 1

    # Ajoutez un bouton pour déclencher la prédiction
    if st.button("Prédire le Prix de l'Assurance"):
        with open('modele.pkl', 'rb') as file:
            grid_search = pickle.load(file)
            dico_params = {'age': [age], 'sex': [sex], 'bmi': [bmi], 'smoker': [smoker], 'children': [children], 'region': [region]}

            input_data = pd.DataFrame(dico_params)

            stupid_encodage = dico_params['sex'][0]
            for stupid in stupid_encodage:
                new_col_name = f'is_{stupid}'
                input_data[new_col_name] = (dico_params['sex'] == stupid).astype(int)
            input_data.rename(columns={'is_0': 'is_male', 'is_1': 'is_female'}, inplace=True)
            input_data['sex'] = 1 if sex == 'Femme' else 0

            idiot_encodage = dico_params['smoker'][0]
            for idiot in idiot_encodage:
                new_col_name = f'is_{idiot}'
                input_data[new_col_name] = (dico_params['smoker'] == idiot).astype(int)
            input_data.rename(columns={'is_fumeur': 'is_smoker', 'non_fumeur': 'is_not_smoker'}, inplace=True)
            input_data['smoker'] = 1 if smoker == 'fumeur' else 0

            imbecile_encodage = dico_params['region'][0]
            for imbecile in imbecile_encodage:
                new_col_name = f'is_{imbecile}'
                input_data[new_col_name] = (dico_params['region'] == imbecile).astype(int)
            input_data.pop('region')

            gremlins_encodage = dico_params['children'][0]
            for gremlins in gremlins_encodage:
                new_col_name = f'children_{gremlins}'
                input_data[new_col_name] = (dico_params['children'] == gremlins).astype(int)

            input_data['Insuffisance pondérale'] = int(bmi < 18.5)
            input_data['Poids normal'] = int(18.5 <= bmi < 24.9)
            input_data['Surpoids'] = int(24.9 <= bmi < 29.9)
            input_data['Obésité de classe I (modérée)'] = int(29.9 <= bmi < 34.9)
            input_data['Obésité de classe II (sévère)'] = int(bmi >= 34.9)

            input_data['Jeune'] = 1 if int(age < 21) else 0
            input_data['Adulte'] = 1 if int(35 <= age < 50) else 0
            input_data['Adulte moyen'] = 1 if int(50 <= age < 65) else 0
            input_data['Senior'] = 1 if int(65 <= age < 75) else 0
            input_data['Très senior'] = 1 if int(age >= 75) else 0

            # Faire la prédiction
            prediction = grid_search.predict(input_data)
            st.write(f"Prédiction des Charges Médicales : {prediction}")

if __name__ == "__main__":
    page_prediction()




