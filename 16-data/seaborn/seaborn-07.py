import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
iris = sns.load_dataset("iris")

# Create a pair plot
sns.pairplot(data=iris, hue="species")

# Show the plot
plt.show()
