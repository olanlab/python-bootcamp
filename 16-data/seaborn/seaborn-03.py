import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a box plot
sns.boxplot(data=tips, x="day", y="total_bill")

# Show the plot
plt.show()
