import matplotlib.pyplot as plt
import numpy as np

# Generate data
theta = np.linspace(0, 2 * np.pi, 100)
r = np.sin(3 * theta)

# Create a polar plot
ax = plt.subplot(111, polar=True)
ax.plot(theta, r)

# Customize the plot
ax.set_title("Polar Plot")

# Display the plot
plt.show()
