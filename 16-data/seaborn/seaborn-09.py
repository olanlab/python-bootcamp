import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
flights = sns.load_dataset("flights")

# Create a time series plot
sns.lineplot(data=flights, x="year", y="passengers", hue="month", marker="o", markersize=5)

# Show the plot
plt.show()
