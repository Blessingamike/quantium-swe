from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('data/pink_morsel_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

fig = px.line(df, x='date', y='sales', color='region',
              labels={'date': 'Date', 'sales': 'Sales ($)', 'region': 'Region'})

fig.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000,
              line_dash='dash', line_color='red',
              annotation_text='Price Increase', annotation_position='top right')

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)