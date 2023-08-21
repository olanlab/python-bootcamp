import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
iris = sns.load_dataset("iris")

# Create a joint distribution plot
sns.jointplot(data=iris, x="sepal_length", y="sepal_width", hue="species")

# Show the plot
plt.show()
