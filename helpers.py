# helpers.py
def select_bmi_column(X):
    return X[['bmi']]

def transform_bmi_features(X):
    return X[['bmi']].assign(
        Insuffisance_pondérale=(X['bmi'] < 18.5).astype(int),
        Poids_normal=((X['bmi'] >= 18.5) & (X['bmi'] < 24.9)).astype(int),
        Surpoids=((X['bmi'] >= 24.9) & (X['bmi'] < 29.9)).astype(int),
        Obésité_de_classe_I_modérée=((X['bmi'] >= 29.9) & (X['bmi'] < 34.9)).astype(int),
        Obésité_de_classe_II_sévère=(X['bmi'] >= 34.9).astype(int)
    )