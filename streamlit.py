import streamlit as st 
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.impute import SimpleImputer



st.title("Projet Assur'Aimant")


st.sidebar.header("Paramètres")
sex = st.sidebar.radio("Sexe", ["male", "female"])
parametre_taille = st.sidebar.slider("Votre taille", 0, 250, 165)
parametre_poids = st.sidebar.slider("Votre Poids", 0, 150, 70)
age = st.sidebar.slider("Votre age", 18, 99, 45)
children = st.sidebar.slider("Nombre d'enfants", 0, 5, 0)
region = st.sidebar.selectbox("Région", ['northwest', 'northeast', 'southwest', 'southeast'])
smoker = st.sidebar.checkbox("Fumeur", False)
bmi = round(parametre_poids / (parametre_taille /100)**2,2)


st.write(f"Votre taille est {parametre_taille}")
st.write(f"Votre poids est {parametre_poids}")
st.write(f"Votre imc est de {bmi}")

if children == 1:
    st.write(f"Vous avez {children} enfant")
elif children == 0:
    st.write(f"Vous n'avez pas d'enfants")
else:
    st.write(f"Vous avez {children} enfants")


st.write(f"Vous habitez au {region}")
st.write(f"Vous êtes {'fumeur' if smoker else 'non fumeur'}")




if st.sidebar.button("Prédire les Charges Médicales"):
    with open('modele.pkl', 'rb') as file:
        model = pickle.load(file)
        smoker_mapping = { True : 'yes', False : 'no'}      
        smoker = smoker_mapping.get(smoker, smoker)

        dico_params = {'age': [age], 'sex': [sex], 'bmi': [bmi], 'smoker': [smoker],
                       'children': [children], 'region': [region]}
         
        input_data = pd.DataFrame(dico_params)
        
        prediction = model.predict(input_data)


    st.write(f"Prédiction des Charges Médicales : {str(prediction)}")

