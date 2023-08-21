import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]

# Create a bar chart
plt.bar(categories, values)

# Customize the plot
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Display the plot
plt.show()
