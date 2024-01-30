import pandas as pd
import matplotlib.pyplot as plt

# Load housing data from task2 folder
data = pd.read_csv('housing_training.csv', header=None)

# Select data from column A (based on the zero-index)
selected_data = data[[0]]

# Create a histogram
plt.hist(selected_data, bins=10)

# Add labels and title
plt.xlabel('A')
plt.ylabel('Count')
plt.title('Histogram of Column A')

# Save the histogram to a PNG file
plt.savefig('task3.png', format='png')

# Show the plot
plt.show()
