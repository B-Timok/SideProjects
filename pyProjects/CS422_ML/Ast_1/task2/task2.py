import pandas as pd
import matplotlib.pyplot as plt

# Load housing data from CSV
data = pd.read_csv('housing_training.csv', header=None)

# Select the columns K, M, and N (based on index)
selected_data = data[[10, 12, 13]]

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