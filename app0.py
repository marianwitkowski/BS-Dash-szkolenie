# Pierwsza "aplikacja" Dash

import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/gdp-life-exp-2007.csv")

app = dash.Dash()
app.layout = html.Div(
    children=[
        html.H1(children='Test Dash'),
        html.Div(children="Przykładowy wykres"),

        dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Przychód'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Koszt'},
                    ],
                    'layout': {
                        'title': 'Tytuł wykresu'
                    }
                }
            ),

        dcc.Graph(
              id='life-exp-vs-gdp',
              figure={
                 'data': [
                    go.Scatter(
                       x=df[df['continent'] == i]['gdp per capita'],
                       y=df[df['continent'] == i]['life expectancy'],
                       text=df[df['continent'] == i]['country'],
                       mode='markers',
                       opacity=0.7,
                       marker={
                          'size': 15,
                          'line': {'width': 0.5, 'color': 'white'}
                       },
                       name=i
                    ) for i in df.continent.unique()
                 ],
                 'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                    yaxis={'title': 'Life Expectancy'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    hovermode='closest'
                 )
              }
           )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=5555)
