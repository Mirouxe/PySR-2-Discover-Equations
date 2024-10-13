# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from pysr import PySRRegressor

# Generate data (for example, a simple function y = x1**2 + x2**3)
X = np.random.randn(100, 1)  # Generate input data with 2 variables
y = X[:, 0]**2 + X[:, 0]**3  # Generate output data according to the function

# Initialize the PySR model
model = PySRRegressor(
    niterations=100,  # Number of iterations for the evolutionary search
    binary_operators=["+", "*", "-", "/"],  # Operators that PySR can use
    unary_operators=["cos", "exp", "sin"],  # Unary functions that PySR can use
    model_selection="best",  # Select the best model in terms of accuracy
)

# Train the model with the data
model.fit(X, y)

# Display all found equations (increasing complexity)
print("Discovered equations:")
print(model)

# Get the best equation (the model with the best score)
best_model = model.get_best()

# Display the analytical expression of the best equation
print("\nBest equation found:")
print(best_model)

# Predict values with the discovered model
y_pred = model.predict(X)

# Plot the true values (y) and the predictions (y_pred) as a function of x1
plt.figure(figsize=(10, 6))

# Plot the true values
plt.scatter(X[:, 0], y, color='blue', marker='o', facecolors='none', label='True values (y): $y = x^2 + x^3$')

# Plot the model predictions
plt.scatter(X[:, 0], y_pred, color='green', marker='x', label='PySR predictions (y_pred)', alpha=0.7)

plt.xlabel("X (Input feature)")
plt.ylabel("Y (Output value)")
plt.title("Comparison of true values and PySR model predictions as a function of x")
plt.legend()
plt.show()
