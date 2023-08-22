import plotly.express as px
import pandas as pd

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 6, 8, 3, 7],
    'label': ['A', 'B', 'C', 'D', 'E']
}

df = pd.DataFrame(data)

# Create an interactive scatter plot
fig = px.scatter(df, x='x', y='y', text='label', title='Interactive Scatter Plot')

# Add labels to the data points
fig.update_traces(textposition='top center')

# Show the plot
fig.show()