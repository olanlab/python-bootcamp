import plotly.express as px
import pandas as pd

# Sample data
data = {
    'labels': ['A', 'B', 'C', 'D', 'E'],
    'values': [10, 6, 8, 3, 7]
}

df = pd.DataFrame(data)

# Create a pie chart
fig = px.pie(df, names='labels', values='values', title='Pie Chart')

# Show the plot
fig.show()
