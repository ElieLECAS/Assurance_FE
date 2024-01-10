import streamlit as st 
import pickle
import numpy as np
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


if parametre_sexe=='Homme':
    parametre_sexe == 0
else:
    parametre_sexe==1

if st.sidebar.button("Prédire les Charges Médicales"):
    with open('modele.pkl', 'rb') as file:
        model = pickle.load(file)

        input_data = np.array([[parametre_sexe,parametre_age, bmi, parametre_fumeur,parametre_enfants,parametre_region]])

        prediction = model.predict(input_data)
    st.write(f"Prédiction des Charges Médicales : {prediction[0]}")
