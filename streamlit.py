import streamlit as st 
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures



st.title("Projet Assur'Aiment")


st.sidebar.header("Paramètres")
parametre_sexe = st.sidebar.radio("Sexe", ["Homme", "Femme"])
parametre_taille = st.sidebar.slider("Votre taille", 0, 250, 165)
parametre_poids = st.sidebar.slider("Votre Poids", 0, 150, 70)
parametre_age = st.sidebar.slider("Votre age", 18, 99, 45)
parametre_enfants = st.sidebar.slider("Nombre d'enfants", 0, 5, 0)
parametre_region = st.sidebar.selectbox("Région", ['NordOuest', 'NordEast', 'SudOuest', 'SudEast'])
parametre_fumeur = st.sidebar.checkbox("Fumeur", False)
bmi = round(parametre_poids / (parametre_taille /100)**2,2)


st.write(f"Votre taille est {parametre_taille}")
st.write(f"Votre poids est {parametre_poids}")
st.write(f"Votre imc est de {bmi}")

if parametre_enfants == 1:
    st.write(f"Vous avez {parametre_enfants} enfant")
elif parametre_enfants == 0:
    st.write(f"Vous n'avez pas d'enfants")
else:
    st.write(f"Vous avez {parametre_enfants} enfants")

st.write(f"Vous habitez au {parametre_region}")
st.write(f"Vous êtes {'fumeur' if parametre_fumeur else 'non fumeur'}")


if st.sidebar.button("Prédire les Charges Médicales"):
    with open('modele.pkl', 'rb') as file:
        grid_search = pickle.load(file)

        dico_params = {'age': [parametre_age], 'sex': [parametre_sexe], 'bmi': [bmi], 'smoker': [parametre_fumeur],
                       'children': [parametre_enfants], 'region': [parametre_region]}

        # Convertir le genre en 1 (Homme) ou 0 (Femme)
        dico_params['is_male'] = 1 if 'Homme' in parametre_sexe else 0
        dico_params['is_female'] = 1 if 'Femme' in parametre_sexe else 0
        dico_params['sex'] = 1 if parametre_sexe == 'Femme' else 0

        dico_params['is_smoker'] = 1 if parametre_fumeur else 0
        dico_params['is_not_smoker'] = 1 if not parametre_fumeur else 0
        dico_params['smoker'] = 1 if parametre_fumeur else 0


        # Ajouter de nouvelles clés et valeurs pour chaque région
        dico_params['NordOuest'] = 1 if 'northwest' in parametre_region else 0
        dico_params['NordEast'] = 1 if 'northeast' in parametre_region else 0
        dico_params['SudOuest'] = 1 if 'southwest' in parametre_region else 0
        dico_params['SudEast'] = 1 if 'southeast' in parametre_region else 0
        dico_params.pop('region')   

        dico_params['children_0'] = 1 if '0' in parametre_region else 0
        dico_params['children_1'] = 1 if '1' in parametre_region else 0
        dico_params['children_2'] = 1 if '2' in parametre_region else 0
        dico_params['children_3'] = 1 if '3' in parametre_region else 0
        dico_params['children_4'] = 1 if '4' in parametre_region else 0
        dico_params['children_5'] = 1 if '5' in parametre_region else 0
       

        dico_params['Insuffisance pondérale'] = int(bmi < 18.5)
        dico_params['Poids normal'] = int(18.5 <= bmi < 24.9)
        dico_params['Surpoids'] = int(24.9 <= bmi < 29.9)
        dico_params['Obésité de classe I (modérée)'] = int(29.9 <= bmi < 34.9)
        dico_params['Obésité de classe II (sévère)'] = int(bmi >= 34.9)

        dico_params['Jeune'] = 1 if int(parametre_age < 21) else 0
        dico_params['Adulte'] = 1 if int(35 <= parametre_age < 50) else 0
        dico_params['Adulte moyen'] = 1 if int(50 <= parametre_age < 65) else 0
        dico_params['Senior'] = 1 if int(65 <= parametre_age < 75) else 0
        dico_params['Très senior'] = 1 if int(parametre_age >= 75) else 0

        input_data = pd.DataFrame(dico_params)

        # input_data_poly = grid_search.best_estimator_.named_steps['polynomialfeatures'].transform(input_data)

        # Faire la prédiction
        # prediction = grid_search.best_estimator_.named_steps['lasso'].predict(input_data_poly)
        prediction = grid_search.predict(input_data)


    st.write(f"Prédiction des Charges Médicales : {prediction}")
