import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the MNIST dataset
mnist = pd.read_csv('MNIST_100.csv')

# Assume the labels are in a column named 'label'
labels = mnist['label']
data = mnist.drop('label', axis=1)

# Preprocess the data by scaling it
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.values)

# Apply PCA to reduce the data dimension to two or three
pca = PCA(n_components=2)  # Change n_components to 3 for three-dimensional visualization
reduced_data = pca.fit_transform(scaled_data)

# Plot the reduced data
plt.figure(figsize=(10, 8))
for i in range(10):
    indices = np.where(labels == i)
    plt.scatter(reduced_data[indices, 0], reduced_data[indices, 1], label=str(i))
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Digit')
plt.title('MNIST Data Visualization using PCA')

# Save the plot to a PNG file
plt.savefig('mnist_task1.png')

plt.show()