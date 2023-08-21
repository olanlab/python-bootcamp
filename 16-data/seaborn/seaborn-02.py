import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
flights = sns.load_dataset("flights")

# Pivot the data to create a matrix
flights_pivot = flights.pivot("month", "year", "passengers")

# Create a heatmap
sns.heatmap(data=flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

# Show the plot
plt.show()