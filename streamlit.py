import streamlit as st 
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler, OneHotEncoder, PolynomialFeatures
from datetime import datetime, timedelta
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Lasso
from helpers import categorize_imc

# st.set_page_config(
#     page_title="Mon Application",
#     page_icon="🧊",
#     layout="wide",
# )

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def page_prediction():

    st.markdown(
        """
        <style>
            .st-cm {
                background-color: #f0f0f0; /* Set your desired background color */
                padding: 20px; /* Optional: Add padding for better appearance */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([0.35, 3])
    col1.image('assets/OIG2-removebg-preview.png', width=100)
    col2.markdown(
        "<h1 style='color: #87CEEB; display: inline-block; vertical-align: middle;'>SSUR'ÉMENT</h1>",
        unsafe_allow_html=True
    )

    st.title("Saisie de Données pour la Prédiction")

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
    st.write(f"Vous êtes {'fumeur' if smoker else 'non fumeur'}")

    poids = st.number_input("Entrez votre Poids (kg)", min_value=0, max_value=150, value=70)
    st.write(f"Votre poids est {poids} kg")

    taille = st.number_input("Entrez votre Taille (cm)", min_value=0, max_value=220, value=170)
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

    categories = {
    'Underweight': (0, 18.5),
    'Normal Weight': (18.5, 24.9),
    'Overweight': (25, 29.9),
    'Obesity Class I': (30, 34.9),
    'Obesity Class II': (35, 39.9),
    'Obesity Class III': (40, float('inf'))
}

    if st.button("Prédire le Prix de l'Assurance"):
        try:
            with open('modele.pkl', 'rb') as file:
                grid_search = pickle.load(file)

                age = calculate_age(birthdate)

                smoker_mapping = { True : 'yes', False : 'no'}
                smoker = smoker_mapping.get(smoker, smoker)

                sex_mapping = {'Homme': 'male', 'Femme': 'female'}
                sex = sex_mapping.get(sex, sex)

                input_data = pd.DataFrame({
                'age': [age],
                'sex': [sex],
                'bmi': [bmi],
                'smoker': [smoker],
                'children': [children],
                'region': [region],
                'imc_category': [categorize_imc(bmi, categories)]  # Assurez-vous que 'categories' est défini
                })

                input_data = input_data.fillna(0)

                print("Input Data:")
                print(input_data)

                prediction = grid_search.predict(input_data)
                st.write(f"Prédiction des Charges Médicales : ${round(float(prediction),2)}")

        except Exception as e:
            st.error(f"Erreur lors du chargement du modèle : {e}")


if __name__ == "__main__":
    page_prediction()
