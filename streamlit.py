import streamlit as st
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
    bmi = st.slider("Indice de Masse Corporelle (BMI)", min_value=10.0, max_value=50.0, value=25.0)

    # Ajoutez un bouton pour déclencher la prédiction
    if st.button("Prédire le Prix de l'Assurance"):
        # Ajoutez ici la logique de prédiction en utilisant les données saisies
        st.success("Prédiction effectuée avec succès !")

if __name__ == "__main__":
    page_prediction()