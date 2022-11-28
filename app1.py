# Kontrolki w Dash

import dash
from dash import dcc
from dash import html
from datetime import date

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

app = dash.Dash(__name__)
app.layout = html.Div([

    html.H1(children="Nagłówek 1", style={"font-size": "44px"}),
    html.P(children="Paragraf"),
    html.A(children="Link", href="http://wp.pl/"),
    html.Hr(),

    dcc.Checklist(
            options={
                'New York City': 'New York City',
                'Montreal': 'Montreal',
                'San Francisco': 'San Francisco'
            },
            value=['Montreal','San Francisco'], style={"margin-top":20, "margin-bottom":20}
    ),
    html.Hr(),

    dcc.RadioItems(['New York City', 'Montreal','San Francisco'], 'Montreal'),
    html.Hr(),

    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        end_date=date(2017, 8, 25),
        style={"margin-top": 20, "margin-bottom": 20}
    ),
    html.Hr(),

    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        date=date(2017, 8, 25),
        style={"margin-top": 20, "margin-bottom": 20}
    ),
    html.Hr(),

    dcc.Slider(0, 20, 5,
               value=10,
               id='my-slider'
               ),
    html.Hr(),

    dcc.Input(id='range', type='number', min=2, max=10, step=1),
    html.Hr(),

    html.Div(
            [
                dcc.Input(
                    id="input_{}".format(_),
                    type=_,
                    placeholder="input type {}".format(_),
                )
                for _ in ALLOWED_TYPES
            ]
            + [html.Div(id="out-all-types")]
        ),

])


if __name__ == '__main__':
    app.run_server(debug=True)