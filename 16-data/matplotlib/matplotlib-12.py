import matplotlib.pyplot as plt
import numpy as np

# Data for line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Data for histogram
data = np.random.normal(0, 1, 1000)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Plot the line plot
ax1.plot(x, y, color='blue')
ax1.set_ylabel('Line Plot')

# Plot the histogram
ax2.hist(data, bins=30, color='red')
ax2.set_xlabel('Values')
ax2.set_ylabel('Histogram')

# Customize the plot
fig.suptitle('Line Plot and Histogram')

# Adjust spacing between subplots
fig.tight_layout()

# Display the plot
plt.show()
