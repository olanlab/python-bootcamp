import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
titanic = sns.load_dataset("titanic")

# Create a bar plot
sns.barplot(data=titanic, x="class", y="fare", hue="who", ci=None)

# Show the plot
plt.show()