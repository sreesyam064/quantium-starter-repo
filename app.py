import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('combined_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])

app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '30px'}, children=[
    html.H1('Pink Morsel Sales Visualiser', style={'textAlign': 'center', 'color': '#7D3C98'}),
    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '15px'}),
        dcc.RadioItems(
            id = 'region-filter',
            options = [
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value = 'all',
            labelStyle = {'textAlign': 'center', 'margin-right': '15px'}
        ),
    ], style = {'textAlign': 'center', 'marginBottom': '30px'}),
    dcc.Graph(id='sales-line-chart'),
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)

def update_chart(selected_region):
    if selected_region == 'all':
        filtered = df
    else:
        filtered = df[df['region'] == selected_region]

    daily_sales = filtered.groupby('date')['sales'].sum().reset_index()


    fig = px.line(daily_sales,
              x='date',
              y='sales',
              title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})" if selected_region != 'all' else "Pink Morsel Sales Over Time (All Regions)",
              labels={'date':'Date', 'sales': 'Total Sales ($)'}
              )

    fig.add_vline(x= pd.to_datetime("2021-01-15"),
              line_dash = 'dash',
              line_color = 'darkred')

    fig.add_annotation(x = pd.to_datetime("2021-01-15"),
                   y = daily_sales['sales'].max(),
                   text = "Price Increases",
                   showarrow = True,
                   arrowhead = 1)

    return fig




if __name__ == '__main__':
    app.run(debug=True)

