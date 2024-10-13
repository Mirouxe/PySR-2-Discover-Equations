# Importer les bibliothèques nécessaires
import numpy as np
import matplotlib.pyplot as plt
from pysr import PySRRegressor

# Générer des données (par exemple, une fonction simple y = x1**2 + x2**3)
X = np.random.randn(100, 1)  # Générer des données d'entrée avec 2 variables
y = X[:, 0]**2 + X[:, 0]**3  # Générer des données de sortie suivant la fonction

# Initialiser le modèle PySR
model = PySRRegressor(
    niterations=100,  # Nombre d'itérations pour la recherche évolutive
    binary_operators=["+", "*", "-", "/"],  # Opérateurs que PySR peut utiliser
    unary_operators=["cos", "exp", "sin"],  # Fonctions unaires que PySR peut utiliser
    model_selection="best",  # Sélectionner le meilleur modèle en termes de précision
)

# Entraîner le modèle avec les données
model.fit(X, y)

# Afficher toutes les équations trouvées (par complexité croissante)
print("Equations découvertes :")
print(model)

# Obtenir la meilleure équation (le modèle avec le meilleur score)
best_model = model.get_best()

# Afficher l'expression analytique de la meilleure équation
print("\nMeilleure équation trouvée :")
print(best_model)

# Prédire les valeurs avec le modèle découvert
y_pred = model.predict(X)

# Tracer les vraies valeurs (y) et les prédictions (y_pred) en fonction de x1
plt.figure(figsize=(10, 6))

# Tracer les vraies valeurs
plt.scatter(X[:, 0], y, color='blue', marker='o', facecolors='none', label='Valeurs réelles (y)')

# Tracer les prédictions du modèle
plt.scatter(X[:, 0], y_pred, color='green', marker='x', label='Prédictions du modèle (y_pred)', alpha=0.7)

plt.xlabel("x1 (Caractéristique d'entrée)")
plt.ylabel("y / y_pred (Valeur de sortie)")
plt.title("Comparaison des valeurs réelles et des prédictions du modèle PySR en fonction de x1")
plt.legend()
plt.show()

