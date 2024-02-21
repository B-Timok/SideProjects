import pandas as pd
import numpy as np
from collections import Counter

# Load datasets
train_data = pd.read_csv('MNIST_training.csv')
test_data = pd.read_csv('MNIST_test.csv')

# Specify the value of K
k = 3

# Select a subset of the data
train_data = train_data.head(100)  # Select the first 100 rows
test_data = test_data.head(10)  # Select the first 10 rows

# Compute distances or similarity
distances = []
for test_index, test_row in test_data.iterrows():
    test_features = test_row.values[1:]  # Exclude the label column
    test_label = test_row['label']
    
    test_distances = []
    for train_index, train_row in train_data.iterrows():
        train_features = train_row.values[1:]  # Exclude the label column
        train_label = train_row['label']
        
        # Compute distance or similarity (e.g., Euclidean, Manhattan, or Cosine similarity)
        distance = np.linalg.norm(test_features - train_features)  # Euclidean distance
        # distance = np.abs(test_features - train_features).sum()  # Manhattan distance
        # distance = 1 - np.dot(test_features, train_features) / (np.linalg.norm(test_features) * np.linalg.norm(train_features))  # Cosine similarity
        
        test_distances.append((distance, train_label))
    
    distances.append((test_label, test_distances))

    # Find the K-nearest neighbors and decide the majority class
    test_distances.sort(key=lambda x: x[0])
    k_nearest_labels = [label for _, label in test_distances[:k]]
    majority_class = Counter(k_nearest_labels).most_common(1)[0][0]
    
    
    print(f"Majority class for test label {test_label} is: {majority_class}")

    # Print distances
    for test_label, test_distances in distances:
        print(f"Distances for test label {test_label}:")
        for distance, train_label in test_distances:
            print(f"Distance: {distance}, Train label: {train_label}")
        print()        
        
        correct_count = 0
        incorrect_count = 0

        for test_label, test_distances in distances:
            predicted_label = Counter([label for _, label in test_distances[:k]]).most_common(1)[0][0]
            
            if predicted_label == test_label:
                correct_count += 1
            else:
                incorrect_count += 1

        print(f"Correctly classified: {correct_count}")
        print(f"Incorrectly classified: {incorrect_count}")
