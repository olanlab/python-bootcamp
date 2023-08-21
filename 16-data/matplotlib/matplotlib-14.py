import matplotlib.pyplot as plt
import numpy as np

# Data for bar chart
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]

# Data for line plot
x = np.arange(len(categories))
y = [0.1, 0.4, 0.2, 0.6]

# Create a figure and axes
fig, ax1 = plt.subplots()

# Plot the bar chart
ax1.bar(x, values, color='blue', label='Bar Chart')

# Customize the plot
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)

# Create a second y-axis for the line plot
ax2 = ax1.twinx()

# Plot the line plot
ax2.plot(x, y, color='red', linestyle='--', marker='o', label='Line Plot')

# Customize the plot
ax2.set_ylabel('Line Plot')
ax2.set_ylim([0, 1])

# Combine the legends
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles, labels)

# Display the plot
plt.title('Bar Chart and Line Plot')
plt.show()