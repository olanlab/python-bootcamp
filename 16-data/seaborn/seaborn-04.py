import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a histogram
sns.histplot(data=tips, x="total_bill", bins=10)

# Show the plot
plt.show()
