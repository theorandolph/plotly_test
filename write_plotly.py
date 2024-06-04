# make sure these are all installed
# !pip install matplotlib seaborn plotly

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

# Generate simulated data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
y2 = np.cos(x) + np.random.normal(0, 0.1, 100)

# Plot using Matplotlib and Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x=x, y=y1, label='Line 1')
sns.lineplot(x=x, y=y2, label='Line 2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simulated Line Chart')
plt.legend()
plt.show()

# Convert to Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Line 1'))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Line 2'))

fig.update_layout(
    title='Simulated Line Chart',
    xaxis_title='X-axis',
    yaxis_title='Y-axis',
    legend_title='Legend',
    width=1200,  # Set width
    height=800   # Set height
)

# Write to an HTML file
pio.write_html(fig, file='line_chart.html', auto_open=True)
