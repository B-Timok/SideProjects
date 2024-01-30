import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Task 1 (PCA)

# Load MNIST dataset
mnist = pd.read_csv('MNIST_100.csv')

# Get data from column named 'label'
labels = mnist['label']
data = mnist.drop('label', axis=1)

# Scale data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.values)

# Apply PCA to reduce the data to two dimensions
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

# Plot data
plt.figure(figsize=(10, 8))
for i in range(10):
    indices = np.where(labels == i)
    plt.scatter(reduced_data[indices, 0], reduced_data[indices, 1], label=str(i))
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Digit')
plt.title('MNIST Data Visualization using PCA')

# Save the plot to a PNG file
plt.savefig('task1.png')

# Show the plot
plt.show()

# ------------------------------------------------------------------

# Task 2 (Boxplot)

# Create new figure
plt.figure()

# Load housing data from CSV
task2_data = pd.read_csv('housing_training.csv', header=None)

# Select the columns K, M, and N (based on index)
selected_data = task2_data[[10, 12, 13]]

# Create boxplot
plt.boxplot(selected_data.values, labels=['K', 'M', 'N'])

# Add labels and title
plt.xlabel('Columns')
plt.ylabel('Values')
plt.title('Boxplot of Columns K, M, and N')

# Save the plot to a PNG file
plt.savefig('task2.png', format='png')

# Show the plot
plt.show()

# ------------------------------------------------------------------

# Task 3 (Histogram)

# Create new figure
plt.figure()

# Load housing data from task2 folder
task3_data = pd.read_csv('housing_training.csv', header=None)

# Select data from column A (based on the zero-index)
selected_data2 = task3_data[[0]]

# Create a histogram
plt.hist(selected_data2, bins=10)

# Add labels and title
plt.xlabel('A')
plt.ylabel('Count')
plt.title('Histogram of Column A')

# Save the histogram to a PNG file
plt.savefig('task3.png', format='png')

# Show the plot
plt.show()
