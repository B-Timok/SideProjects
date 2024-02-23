import numpy as np
import pandas as pd
from collections import Counter

# Step 1: Load the training and test data
train_data = pd.read_csv("MNIST_training.csv")
test_data = pd.read_csv("MNIST_test.csv")

# Define a function to calculate Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))

# Define a function to compute accuracy
def compute_accuracy(K):
    # Step 2: Define the value of K
    # K = 5

    # Step 3: Compute distances/similarities between test and training data
    distances = np.zeros((test_data.shape[0], train_data.shape[0]))
    for i in range(test_data.shape[0]):
        distances[i] = euclidean_distance(test_data.values[i, 1:], train_data.values[:, 1:])

    # Step 4: Find K-nearest neighbors and decide majority class
    knn_indices = np.argpartition(distances, K, axis=1)[:, :K]
    knn_labels = train_data.values[knn_indices, 0]
    predicted_labels = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=1, arr=knn_labels)

    # Step 5: Compare prediction with ground truth
    ground_truth = test_data.values[:, 0]
    correctly_classified = np.sum(predicted_labels == ground_truth)
    incorrectly_classified = np.sum(predicted_labels != ground_truth)

    # Step 6: Compute accuracy
    accuracy = correctly_classified / len(test_data)

    print(f"K: {K}, Accuracy: {accuracy * 100}%")

# Test for different values of K
K_values = [3, 7, 9]
for K in K_values:
    compute_accuracy(K)