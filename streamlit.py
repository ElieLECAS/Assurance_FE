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
    
    birthdate = st.date_input("Date de Naissance", format="DD/MM/YYYY")
    age = calculate_age(birthdate)
    st.write(f"Âge actuel : {age} ans")

    sex = st.radio("Sexe", ["Homme", "Femme"])

    smoker = st.checkbox("Êtes-vous Fumeur", False)
    st.write(f"Vous êtes {'fumeur' if smoker else 'non_fumeur'}")

    poids = st.number_input("Entrez votre Poids (kg)", min_value=0.00, max_value=150.00, value=70.00)
    st.write(f"Votre poids est {poids} kg")

    taille = st.number_input("Entrez votre Taille (cm)", min_value=0.00, max_value=220.00, value=170.00)
    st.write(f"Votre taille est {taille/100} m")

    bmi = round(poids / (taille /100)**2,2)
    st.write(f"Votre imc est de {bmi}")

    children = st.number_input("Entrez le nombre(s) d'enfant(s)", min_value=0, value=0)
    if children == 1:
        st.write(f"Vous avez {children} enfant")
    elif children == 0:
        st.write(f"Vous n'avez pas d'enfants")
    else:
        st.write(f"Vous avez {children} enfants")

    
    region = st.selectbox("Sélectionnez une region", ["northwest", "northeast", "southwest", "southeast"])
    
   
    st.write(f"Vous habitez au {region}")
    
    if sex == 'Homme':
        sex = 0
    else:
        sex = 1

    
    if st.button("Prédire le Prix de l'Assurance"):
       
        with open('modele.pkl', 'rb') as file:
            model = pickle.load(file)
            
            input_data = np.array([[sex, age, bmi, smoker, children, region]])

            prediction = model.predict(input_data)
            st.write(f"Prédiction des Charges Médicales : {prediction[0]}")
            
            if st.sidebar.button("Prédire les Charges Médicales"):
                with open('modele.pkl', 'rb') as file:
                    grid_search = pickle.load(file)
                    dico_params = {'age': [age], 'sex': [sex], 'bmi': [bmi], 'smoker': [smoker], 'children': [children], 'region': [region]}
                    
                    stupid_encodage = dico_params['sex'][0]
                    for stupid in stupid_encodage:
                        new_col_name = f'is_{stupid}'
                        dico_params[new_col_name] = (dico_params['sex'] == stupid).astype(int)
                    dico_params.rename(columns={'is_Homme': 'is_male', 'is_Femme': 'is_female'}, inplace=True)
                    dico_params['sex'] = 1 if sex == 'Femme' else 0

                    idiot_encodage = dico_params['smoker'][0]
                    for idiot in idiot_encodage:
                        new_col_name = f'is_{idiot}'
                        dico_params[new_col_name] = (dico_params['smoker'] == idiot).astype(int)
                    dico_params.rename(columns={'is_fumeur': 'is_smoker', 'non_fumeur': 'is_not_smoker'}, inplace=True)
                    dico_params['smoker'] = 1 if smoker == 'fumeur' else 0

                    imbecile_encodage = dico_params['region'][0]
                    for imbecile in imbecile_encodage:
                        new_col_name = f'is_{imbecile}'
                        dico_params[new_col_name] = (dico_params['region'] == imbecile).astype(int)
                    dico_params.pop('region')

                    gremlins_encodage = dico_params['children'][0]
                    for gremlins in gremlins_encodage:
                        new_col_name = f'children_{gremlins}'
                        dico_params[new_col_name] = (dico_params['children'] == gremlins).astype(int)

                    dico_params['Insuffisance pondérale'] = int(bmi < 18.5)
                    dico_params['Poids normal'] = int(18.5 <= bmi < 24.9)
                    dico_params['Surpoids'] = int(24.9 <= bmi < 29.9)
                    dico_params['Obésité de classe I (modérée)'] = int(29.9 <= bmi < 34.9)
                    dico_params['Obésité de classe II (sévère)'] = int(bmi >= 34.9)
                     
                    dico_params['Jeune'] = 1 if int(age < 21) else 0
                    dico_params['Adulte'] = 1 if int(35 <= age < 50) else 0
                    dico_params['Adulte moyen'] = 1 if int(50 <= age < 65) else 0
                    dico_params['Senior'] = 1 if int(65 <= age < 75) else 0
                    dico_params['Très senior'] = 1 if int(age >= 75) else 0

                    input_data = pd.DataFrame(dico_params)
                    #input_data_poly = grid_search.best_estimator_.named_steps['polynomialfeatures'].transform(input_data)
                    # Faire la prédiction
                    # prediction = grid_search.best_estimator_.named_steps['lasso'].predict(input_data_poly)
                    prediction = grid_search.predict(input_data)


        st.write(f"Prédiction des Charges Médicales : {str(prediction)}")

if __name__ == "__main__":
    page_prediction()



# st.title("Projet Assur'Aimant")


# st.sidebar.header("Paramètres")
# parametre_sexe = st.sidebar.radio("Sexe", ["Homme", "Femme"])
# parametre_taille = st.sidebar.slider("Votre taille", 0, 250, 165)
# parametre_poids = st.sidebar.slider("Votre Poids", 0, 150, 70)
# parametre_age = st.sidebar.slider("Votre age", 18, 99, 45)
# parametre_enfants = st.sidebar.slider("Nombre d'enfants", 0, 5, 0)
# parametre_region = st.sidebar.selectbox("Région", ['NordOuest', 'NordEast', 'SudOuest', 'SudEast'])
# parametre_fumeur = st.sidebar.checkbox("Fumeur", False)
# bmi = round(parametre_poids / (parametre_taille /100)**2,2)


# st.write(f"Votre taille est {parametre_taille}")
# st.write(f"Votre poids est {parametre_poids}")
# st.write(f"Votre imc est de {bmi}")

# if parametre_enfants == 1:
#     st.write(f"Vous avez {parametre_enfants} enfant")
# elif parametre_enfants == 0:
#     st.write(f"Vous n'avez pas d'enfants")
# else:
#     st.write(f"Vous avez {parametre_enfants} enfants")

# st.write(f"Vous habitez au {parametre_region}")
# st.write(f"Vous êtes {'fumeur' if parametre_fumeur else 'non fumeur'}")


# if st.sidebar.button("Prédire les Charges Médicales"):
#     with open('modele.pkl', 'rb') as file:
#         grid_search = pickle.load(file)

#         dico_params = {'age': [parametre_age], 'sex': [parametre_sexe], 'bmi': [bmi], 'smoker': [parametre_fumeur],
#                        'children': [parametre_enfants], 'region': [parametre_region]}

#         # Convertir le genre en 1 (Homme) ou 0 (Femme)
#         dico_params['is_male'] = 1 if 'Homme' in parametre_sexe else 0
#         dico_params['is_female'] = 1 if 'Femme' in parametre_sexe else 0
#         dico_params['sex'] = 1 if parametre_sexe == 'Femme' else 0

#         dico_params['is_smoker'] = 1 if parametre_fumeur else 0
#         dico_params['is_not_smoker'] = 1 if not parametre_fumeur else 0
#         dico_params['smoker'] = 1 if parametre_fumeur else 0


#         # Ajouter de nouvelles clés et valeurs pour chaque région
#         dico_params['NordOuest'] = 1 if 'northwest' in parametre_region else 0
#         dico_params['NordEast'] = 1 if 'northeast' in parametre_region else 0
#         dico_params['SudOuest'] = 1 if 'southwest' in parametre_region else 0
#         dico_params['SudEast'] = 1 if 'southeast' in parametre_region else 0
#         dico_params.pop('region')   

#         dico_params['children_0'] = 1 if '0' in parametre_region else 0
#         dico_params['children_1'] = 1 if '1' in parametre_region else 0
#         dico_params['children_2'] = 1 if '2' in parametre_region else 0
#         dico_params['children_3'] = 1 if '3' in parametre_region else 0
#         dico_params['children_4'] = 1 if '4' in parametre_region else 0
#         dico_params['children_5'] = 1 if '5' in parametre_region else 0
       

#         dico_params['Insuffisance pondérale'] = int(bmi < 18.5)
#         dico_params['Poids normal'] = int(18.5 <= bmi < 24.9)
#         dico_params['Surpoids'] = int(24.9 <= bmi < 29.9)
#         dico_params['Obésité de classe I (modérée)'] = int(29.9 <= bmi < 34.9)
#         dico_params['Obésité de classe II (sévère)'] = int(bmi >= 34.9)

#         dico_params['Jeune'] = 1 if int(parametre_age < 21) else 0
#         dico_params['Adulte'] = 1 if int(35 <= parametre_age < 50) else 0
#         dico_params['Adulte moyen'] = 1 if int(50 <= parametre_age < 65) else 0
#         dico_params['Senior'] = 1 if int(65 <= parametre_age < 75) else 0
#         dico_params['Très senior'] = 1 if int(parametre_age >= 75) else 0

#         input_data = pd.DataFrame(dico_params)

#         # input_data_poly = grid_search.best_estimator_.named_steps['polynomialfeatures'].transform(input_data)

#         # Faire la prédiction
#         # prediction = grid_search.best_estimator_.named_steps['lasso'].predict(input_data_poly)
#         prediction = grid_search.predict(input_data)


#     st.write(f"Prédiction des Charges Médicales : {str(prediction)}")
