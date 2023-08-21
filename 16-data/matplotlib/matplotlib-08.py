import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = np.random.rand(10, 10)

# Create a heatmap
plt.imshow(data, cmap='hot', interpolation='nearest')

# Add colorbar
plt.colorbar()

# Customize the plot
plt.title("Heatmap")

# Display the plot
plt.show()
