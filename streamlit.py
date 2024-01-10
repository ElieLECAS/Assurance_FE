import streamlit as st 
import pickle
import numpy as np
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
