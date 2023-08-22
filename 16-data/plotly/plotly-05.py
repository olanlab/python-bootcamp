import plotly.express as px
import pandas as pd

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 6, 8, 3, 7],
    'z': [5, 9, 2, 6, 4]
}

df = pd.DataFrame(data)

# Create a 3D scatter plot
fig = px.scatter_3d(df, x='x', y='y', z='z', title='3D Scatter Plot')

# Show the plot
fig.show()
