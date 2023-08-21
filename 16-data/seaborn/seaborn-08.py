import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
titanic = sns.load_dataset("titanic")

# Create a facet grid
g = sns.FacetGrid(data=titanic, col="class", row="survived")
g.map(sns.histplot, "age")

# Show the plot
plt.show()
