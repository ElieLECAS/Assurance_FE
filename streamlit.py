import streamlit as st 
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime, timedelta

def page_accueil():
    st.title("Assur'ément - Estimation des Primes d'Assurance")

    st.write(
        "Bienvenue dans l'application Assur'ément, une solution d'estimation des primes d'assurance."
    )

    st.write(
        "Cette application vous permet d'explorer les données, de visualiser des analyses et de faire des prédictions sur les primes d'assurance en fonction des données démographiques."
    )

    st.write(
        "Utilisez le menu sur la gauche pour naviguer entre les différentes sections de l'application."
    )

    st.write("Pour commencer, sélectionnez l'onglet 'Exploration des Données'.")

    # Ajoutez un bouton pour rediriger vers la deuxième page
    if st.button("Entrer des Données pour la Prédiction"):
        st.session_state.page = "page_prediction"

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def page_prediction():
    st.title("Assur'ément - Saisie de Données pour la Prédiction")

    st.write(
        "Utilisez cette page pour entrer les données nécessaires à la prédiction du prix de l'assurance."
    )

    # Ajoutez un champ de sélection de date pour la date de naissance avec le format jour-mois-année
    birthdate = st.date_input("Date de Naissance", format="DD/MM/YYYY")

    # Calculez automatiquement l'âge en fonction de la date de naissance
    age = calculate_age(birthdate)

    # Affichez l'âge calculé
    st.write(f"Âge actuel : {age} ans")

    # Ajoutez ici d'autres champs de saisie des données (sex, bmi, etc.)
    sex = st.radio("Sexe", ["Homme", "Femme"])

    smoker = st.radio("Êtes-vous Fumeur", ["non_Fumeur", "Fumeur"])

    poids = st.number_input("Entrez votre Poids (kg)", min_value=0.00, max_value=150.00, value=70.00)
    st.write(f"Votre poids est {poids} kg")

    taille = st.number_input("Entrez votre Taille (cm)", min_value=0.00, max_value=220.00, value=170.00)
    st.write(f"Votre taille est {taille/100} m")

    bmi = round(poids / (taille /100)**2,2)
    st.write(f"Votre imc est de {bmi}")


    children = st.number_input("Entrez le nombre(s) d'enfant(s)", min_value=0, value=0)
    st.write(f"Vous avez {children} enfant(s)")


    # Ajoutez un champ de sélection avec 4 options
    region = st.selectbox("Sélectionnez une region", ["northwest", "northeast", "southwest", "southeast"])
    
    # Affichez la valeur sélectionnée
    st.write(f"Option sélectionnée : {region}")
    

    # Ajoutez un bouton pour déclencher la prédiction
    if st.button("Prédire le Prix de l'Assurance"):
        # Ajoutez ici la logique de prédiction en utilisant les données saisies
        st.success("Prédiction effectuée avec succès !")

if __name__ == "__main__":
    page_prediction()











# parametre_enfants = st.sidebar.slider("Nombre d'enfants", 0, 5, 0)
# parametre_region = st.sidebar.selectbox("Région", ['NordOuest', 'NordEast', 'SudOuest', 'SudEast'])
# parametre_fumeur = st.sidebar.checkbox("Fumeur", False)




# if parametre_enfants == 1:
#     st.write(f"Vous avez {parametre_enfants} enfant")
# elif parametre_enfants == 0:
#     st.write(f"Vous n'avez pas d'enfants")
# else:
#     st.write(f"Vous avez {parametre_enfants} enfants")

# st.write(f"Vous habitez au {parametre_region}")
# st.write(f"Vous êtes {'fumeur' if parametre_fumeur else 'non fumeur'}")


# if parametre_sexe=='Homme':
#     parametre_sexe == 0
# else:
#     parametre_sexe==1

# if st.sidebar.button("Prédire les Charges Médicales"):
#     with open('modele.pkl', 'rb') as file:
#         model = pickle.load(file)

#         input_data = np.array([[parametre_sexe,parametre_age, bmi, parametre_fumeur,parametre_enfants,parametre_region]])

#         prediction = model.predict(input_data)
#     st.write(f"Prédiction des Charges Médicales : {prediction[0]}")
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


#     st.write(f"Prédiction des Charges Médicales : {prediction}")
