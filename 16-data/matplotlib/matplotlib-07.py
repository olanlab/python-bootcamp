import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

# Create a box plot
plt.boxplot(data)

# Customize the plot
plt.title("Box Plot")
plt.xlabel("Data")
plt.ylabel("Value")

# Display the plot
plt.show()
