import matplotlib.pyplot as plt

# Data for bar chart
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]

# Data for pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 25, 10]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot the bar chart
ax1.bar(categories, values, color='blue')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values')
ax1.set_title('Bar Chart')

# Plot the pie chart
ax2.pie(sizes, labels=labels, autopct='%1.1f%%')
ax2.set_title('Pie Chart')

# Customize the plot
fig.suptitle('Bar Chart and Pie Chart')

# Adjust spacing between subplots
fig.tight_layout()

# Display the plot
plt.show()
