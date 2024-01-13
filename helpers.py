# helpers.py
def select_bmi_column(X):
    return X[['bmi']]

def select_age_column(X):
    return X[['age']]

def transform_bmi_features(X):
    return X[['bmi']].assign(
        Insuffisance_pondérale=(X['bmi'] < 18.5).astype(int),
        Poids_normal=((X['bmi'] >= 18.5) & (X['bmi'] < 24.9)).astype(int),
        Surpoids=((X['bmi'] >= 24.9) & (X['bmi'] < 29.9)).astype(int),
        Obésité_de_classe_I_modérée=((X['bmi'] >= 29.9) & (X['bmi'] < 34.9)).astype(int),
        Obésité_de_classe_II_sévère=(X['bmi'] >= 34.9).astype(int)
    )

def transform_age_features(X):
    return X[['age']].assign(
        Jeune=(X['age'] < 18).astype(int),
        Adulte=((X['age'] >= 18) & (X['age'] < 35)).astype(int),
        Adulte_moyen=((X['age'] >= 35) & (X['age'] < 50)).astype(int),
        Senior=((X['age'] >= 50) & (X['age'] < 65)).astype(int),
        Très_senior=(X['age'] >= 65).astype(int)
    )
