import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = np.random.normal(0, 1, 1000)

# Create a histogram
plt.hist(data, bins=30)

# Customize the plot
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Display the plot
plt.show()
