import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the line plot
ax.plot(x, y1, color='blue', label='Sin(x)')

# Plot the scatter plot
ax.scatter(x, y2, color='red', label='Cos(x)')

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Line Plot and Scatter Plot')
ax.legend()

# Display the plot
plt.show()
