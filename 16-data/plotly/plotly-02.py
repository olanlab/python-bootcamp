import plotly.express as px
import pandas as pd

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 6, 8, 3, 7]
}

df = pd.DataFrame(data)

# Create a line chart
fig = px.line(df, x='x', y='y', title='Line Chart')

# Show the plot
fig.show()
