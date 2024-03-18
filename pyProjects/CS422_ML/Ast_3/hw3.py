import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('auto+mpg/auto-mpg.data', sep='\s+', header=None)

# Drop the 'car name' column
data = data.drop(columns=[8])

# Extract the features and target variable
X = data.iloc[:, 1:]
y = data.iloc[:, 0]

# Convert all columns to numeric, coercing errors to NaN
X = X.apply(pd.to_numeric, errors='coerce')

# Handle NaN values. Here, we're dropping rows with any NaN values.
# You might want to handle this differently depending on your dataset.
X = X.dropna()

# Now you can normalize
X = (X - X.mean()) / X.std()

# Add a column of ones to X for the bias term
X = np.c_[np.ones(X.shape[0]), X]

# Initialize the parameters
theta = np.zeros(X.shape[1])

# Define the cost function
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

# Define the gradient descent function
def gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    costs = []
    for i in range(num_iterations):
        predictions = X.dot(theta)
        theta -= (learning_rate / m) * (X.T.dot(predictions - y))
        costs.append(compute_cost(X, y, theta))
    return theta, costs

# Implement 10-fold cross-validation
kf = KFold(n_splits=10)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    theta, _ = gradient_descent(X_train, y_train, theta, 0.01, 1000)
    predictions = X_test.dot(theta)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    print(f'Coefficients: {theta[1:]}, RMSE: {rmse}')