import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1)

# Plot data on subplots
ax1.plot(x, y1)
ax1.set_ylabel('Sin(x)')
ax2.plot(x, y2)
ax2.set_xlabel('x')
ax2.set_ylabel('Cos(x)')

# Customize the plot
fig.suptitle('Subplots')

# Adjust spacing between subplots
fig.tight_layout()

# Display the plot
plt.show()
