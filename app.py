from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('data/pink_morsel_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser',
            style={
                'textAlign': 'center',
                'color': '#ff69b4',
                'fontFamily': 'Arial, sans-serif',
                'padding': '20px',
                'borderBottom': '2px solid #ff69b4'
            }),

    html.Div([
        html.Label('Filter by Region:',
                   style={'fontFamily': 'Arial', 'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'fontFamily': 'Arial', 'fontSize': '16px'},
            labelStyle={'marginRight': '20px'}
        )
    ], style={
        'textAlign': 'center',
        'padding': '20px',
        'backgroundColor': '#fff0f5',
        'margin': '20px'
    }),

    dcc.Graph(id='sales-chart')

], style={'backgroundColor': '#fff8fc', 'minHeight': '100vh'})


@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_chart(region):
    filtered = df if region == 'all' else df[df['region'] == region]

    fig = px.line(filtered, x='date', y='sales', color='region',
                  labels={'date': 'Date', 'sales': 'Sales ($)', 'region': 'Region'})

    fig.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000,
                  line_dash='dash', line_color='red',
                  annotation_text='Price Increase', annotation_position='top right')

    fig.update_layout(
        plot_bgcolor='#fff0f5',
        paper_bgcolor='#fff8fc',
        font=dict(family='Arial', color='#333'),
        hovermode='x unified'
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)