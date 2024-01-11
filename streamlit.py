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

            input_data['is_male'] = (input_data['sex'] == 0).astype(int)
            input_data['is_female'] = (input_data['sex'] == 1).astype(int)
            input_data['sex'].replace(['Homme', 'Femme'], [0,1], inplace=True)
            # stupid_encodage = dico_params['sex'][0]
            # for stupid in stupid_encodage:
            #     new_col_name = f'is_{stupid}'
            #     input_data[new_col_name] = (dico_params['sex'] == stupid).astype(int)
            # input_data.rename(columns={'is_0': 'is_male', 'is_1': 'is_female'}, inplace=True)
            # input_data['sex'] = 1 if sex == 'Femme' else 0

            input_data['smoker'].replace([False, True], [0,1], inplace=True)
            input_data['is_smoker'] = (input_data['smoker'] == 1).astype(int)
            input_data['is_not_smoker'] = (input_data['smoker'] == 1).astype(int)
            # idiot_encodage = dico_params['smoker'][0]
            # for idiot in idiot_encodage:
            #     new_col_name = f'is_{idiot}'
            #     input_data[new_col_name] = (dico_params['smoker'] == idiot).astype(int)
            # input_data.rename(columns={'is_fumeur': 'is_smoker', 'non_fumeur': 'is_not_smoker'}, inplace=True)
            # input_data['smoker'] = 1 if smoker == 'fumeur' else 0

            imbecile_encodage = input_data['region'].unique()
            for imbecile in imbecile_encodage:
                new_col_name = f'is_{imbecile}'
                input_data[new_col_name] = (input_data['region'] == imbecile).astype(int)
            input_data.pop('region')

            gremlins_encodage = input_data['children'].unique()
            for gremlins in gremlins_encodage:
                new_col_name = f'children_{gremlins}'
                input_data[new_col_name] = (input_data['children'] == gremlins).astype(int)

                input_data['Insuffisance pondérale'] = (input_data['bmi'] < 18.5).astype(int)
                input_data['Poids normal'] = ((input_data['bmi'] >= 18.5) & (input_data['bmi'] < 24.9)).astype(int)
                input_data['Surpoids'] = ((input_data['bmi'] >= 24.9) & (input_data['bmi'] < 29.9)).astype(int)
                input_data['Obésité de classe I (modérée)'] = ((input_data['bmi'] >= 29.9) & (input_data['bmi'] < 34.9)).astype(int)
                input_data['Obésité de classe II (sévère)'] = (input_data['bmi'] >= 34.9).astype(int)

                input_data['Jeune'] = (input_data['age'] < 21).astype(int)
                input_data['Adulte'] = ((input_data['age'] >= 35) & (input_data['age'] < 50)).astype(int)
                input_data['Adulte moyen'] = ((input_data['age'] >= 50) & (input_data['age'] < 65)).astype(int)
                input_data['Senior'] = ((input_data['age'] >= 65) & (input_data['age'] < 75)).astype(int)
                input_data['Très senior'] = (input_data['age'] >= 75).astype(int)



            # Faire la prédiction
            prediction = grid_search.predict(input_data)
            st.write(f"Prédiction des Charges Médicales : {prediction}")

if __name__ == "__main__":
    page_prediction()





# st.sidebar.header("Paramètres")
# sex = st.sidebar.radio("Sexe", ["Homme", "Femme"])
# parametre_taille = st.sidebar.slider("Votre taille", 0, 250, 165)
# parametre_poids = st.sidebar.slider("Votre Poids", 0, 150, 70)
# age = st.sidebar.slider("Votre age", 18, 99, 45)
# children = st.sidebar.slider("Nombre d'enfants", 0, 5, 0)
# parametre_region = st.sidebar.selectbox("Région", ['NordOuest', 'NordEast', 'SudOuest', 'SudEast'])
# smoker = st.sidebar.checkbox("Fumeur", False)
# bmi = round(parametre_poids / (parametre_taille /100)**2,2)
# rmse = 4152.91


# st.write(f"Votre taille est {parametre_taille}")
# st.write(f"Votre poids est {parametre_poids}")
# st.write(f"Votre imc est de {bmi}")

# if children == 1:
#     st.write(f"Vous avez {children} enfant")
# elif children == 0:
#     st.write(f"Vous n'avez pas d'enfants")
# else:
#     st.write(f"Vous avez {children} enfants")




# st.write(f"Vous habitez au {parametre_region}")
# st.write(f"Vous êtes {'fumeur' if smoker else 'non fumeur'}")


# if st.sidebar.button("Prédire les Charges Médicales"):
#     with open('modele.pkl', 'rb') as file:
#         grid_search = pickle.load(file)

#         dico_params = {'age': [age], 'sex': [sex], 'bmi': [bmi], 'smoker': [smoker],
#                        'children': [children], 'region': [parametre_region]}
 

#         dico_params['children_0'] = 1 if 0 in [children] else 0
#         dico_params['children_1'] = 1 if 1 in [children] else 0
#         dico_params['children_2'] = 1 if 2 in [children] else 0
#         dico_params['children_3'] = 1 if 3 in [children] else 0
#         dico_params['children_4'] = 1 if 4 in [children] else 0
#         dico_params['children_5'] = 1 if 5 in [children] else 0

        
#         input_data = pd.DataFrame(dico_params)


#         input_data['Insuffisance pondérale'] = (input_data['bmi'] < 18.5).astype(int)
#         input_data['Poids normal'] = ((input_data['bmi'] >= 18.5) & (input_data['bmi'] < 24.9)).astype(int)
#         input_data['Surpoids'] = ((input_data['bmi'] >= 24.9) & (input_data['bmi'] < 29.9)).astype(int)
#         input_data['Obésité de classe I (modérée)'] = ((input_data['bmi'] >= 29.9) & (input_data['bmi'] < 34.9)).astype(int)
#         input_data['Obésité de classe II (sévère)'] = (input_data['bmi'] >= 34.9).astype(int)

#         input_data['Jeune'] = (input_data['age'] < 21).astype(int)
#         input_data['Adulte'] = ((input_data['age'] >= 35) & (input_data['age'] < 50)).astype(int)
#         input_data['Adulte moyen'] = ((input_data['age'] >= 50) & (input_data['age'] < 65)).astype(int)
#         input_data['Senior'] = ((input_data['age'] >= 65) & (input_data['age'] < 75)).astype(int)
#         input_data['Très senior'] = (input_data['age'] >= 75).astype(int)


#         input_data['is_male'] = (input_data['sex'] == 0).astype(int)
#         input_data['is_female'] = (input_data['sex'] == 1).astype(int)
#         input_data['sex'].replace(['Homme', 'Femme'], [0,1], inplace=True)

#         input_data['is_northwest'] = input_data['region'].str.contains('northwest').astype(int)
#         input_data['is_northeast'] = input_data['region'].str.contains('northeast').astype(int)
#         input_data['is_southwest'] = input_data['region'].str.contains('southwest').astype(int)
#         input_data['is_southeast'] = input_data['region'].str.contains('southeast').astype(int)
#         input_data = input_data.drop('region', axis=1)

#         input_data['smoker'].replace([False, True], [0,1], inplace=True)
#         input_data['is_smoker'] = (input_data['smoker'] == 1).astype(int)
#         input_data['is_not_smoker'] = (input_data['smoker'] == 1).astype(int)

#         # input_data_poly = grid_search.best_estimator_.named_steps['polynomialfeatures'].transform(input_data)

#         # prediction = grid_search.best_estimator_.named_steps['lasso'].predict(input_data_poly)
#         # prediction = np.sqrt(prediction)
#         prediction = grid_search.predict(input_data)


#     st.write(f"Prédiction des Charges Médicales : {str(prediction - rmse)}")

