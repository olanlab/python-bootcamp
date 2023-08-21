import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a violin plot with swarm points
sns.violinplot(data=tips, x="day", y="total_bill", inner=None)
sns.swarmplot(data=tips, x="day", y="total_bill", color="white", edgecolor="gray")

# Show the plot
plt.show()
