import plotly.express as px
import pandas as pd

# Sample data
data = {
    'x': ['A', 'B', 'A', 'B', 'A', 'B'],
    'y': [10, 15, 8, 12, 5, 20]
}

df = pd.DataFrame(data)

# Create a box plot
fig = px.box(df, x='x', y='y', title='Box Plot')

# Show the plot
fig.show()
