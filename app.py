import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv('combined_sales_data.csv')

df['date'] = pd.to_datetime(df['date'])

daily_sales = df.groupby('date')['sales'].sum().reset_index()

fig = px.line(daily_sales,
              x='date',
              y='sales',
              title='Pink Morsel Sales Over Time',
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

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Pink Morsel Sales Visualiser', style={'textAlign': 'center'}),dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run(debug=True)

