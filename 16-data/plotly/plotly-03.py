import plotly.express as px
import pandas as pd

# Sample data
data = {
    'x': ['A', 'B', 'C', 'D', 'E'],
    'y': [10, 6, 8, 3, 7]
}

df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(df, x='x', y='y', title='Bar Chart')

# Show the plot
fig.show()
