# Obsługa callback'ów

import dash
from dash import dcc
from dash import html
from dash import Input, Output

external_css = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(__name__, external_stylesheets=external_css)

app.layout = html.Div([
    html.H4("Zmień wartość początkową"),
    html.Div([
        "Input:",
        dcc.Input(id='my-input', type='text', value='')
    ]),
    html.Br(),
    html.Div(id='my-output')
], style={"margin" : 40})


@app.callback(
    Output(component_id="my-output", component_property="children"),
    Input(component_id="my-input", component_property="value")
)
def update_div(input_value):
    return f"A oto wynik: {input_value.upper()}"


if __name__ == '__main__':
    app.run_server(debug=True)