import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Customize the plot
plt.title("Pie Chart")

# Display the plot
plt.show()
