import streamlit as st 
import pickle
import numpy as np
import pandas as pd



col1, col2 = st.columns([0.5, 3])
icon_url = "assets\logo_image.png"
col1.image(icon_url, width=100)
col2.title("Projet Assur'émant")

st.sidebar.header("Paramètres")
sex = st.sidebar.radio("Sexe", ["Homme", "Femme"])
parametre_taille = st.sidebar.slider("Votre taille", 0, 250, 165)
parametre_poids = st.sidebar.slider("Votre Poids", 0, 150, 70)
age = st.sidebar.slider("Votre age", 18, 99, 45)
children = st.sidebar.slider("Nombre d'enfants", 0, 5, 0)
region = st.sidebar.selectbox("Région", ['northwest', 'northeast', 'southwest', 'southeast'])
smoker = st.sidebar.checkbox("Fumeur", False)
bmi = round(parametre_poids / (parametre_taille /100)**2,2)
imc_category = None

sex_mapping = {'Homme': 'male', 'Femme': 'female'}
sex = sex_mapping.get(sex, sex)

smoker_mapping = {True: 'yes', False: 'no'}
smoker = smoker_mapping.get(smoker, smoker)
    

if bmi <= 18.5:
    imc_category = 'Underweight'
elif bmi <= 24.9:
    imc_category = 'Normal Weight'
elif bmi <= 29.9:
    imc_category = 'Overweight'
elif bmi <= 34.9:
    imc_category = 'Obesity Class I'
elif bmi <= 39.9:
    imc_category = 'Obesity Class II'
elif bmi >= 40:
    imc_category = 'Obesity Class III'


st.write(f"Votre taille est {parametre_taille}")
st.write(f"Votre poids est {parametre_poids}")
st.write(f"Votre catégorie d'imc est {bmi}")
st.write(f"Votre imc est {imc_category}")

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

        dico_params = {'age': [age], 'sex': [sex], 'imc_category': [imc_category], 'smoker': [smoker],
                       'children': [children], 'region': [region]}
         
        input_data = pd.DataFrame(dico_params)
        
        prediction = model.predict(input_data)


    st.write(f"Prédiction des Charges Médicales : ${round(float(prediction),2)}")