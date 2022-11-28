
# Wizualizacja danych sprzedażowych
import os
import dash
import numpy as np
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

data = pd.read_csv("data/sales.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_css = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    }
]

external_js = [
    "https://cdn.plot.ly/plotly-locale-pl-latest.js"
]

debug = False if os.environ.get("DASH_DEBUG_MODE") == "False" else True


app = dash.Dash(__name__,
                external_stylesheets=external_css,
                external_scripts=external_js)
server = app.server

app.title = "Sprzedaż awokado"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children=[
                    html.Img(src="assets/awokado.jpg")
                ], className="header-emoji"),
                html.H1(
                    children="Sprzedaż awokado", className="header-title"
                ),
                html.P(
                    children="Wizualizacja sprzedaży owoców",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Sklep", className="menu-title"),
                        dcc.Dropdown(
                            id="shop-filter",
                            options=[
                                {"label": shop, "value": shop}
                                for shop in np.sort(data.shop.unique())
                            ],
                            value=sorted(data.shop.unique())[0],
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Rodzaj", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {"label": avocado_type, "value": avocado_type}
                                for avocado_type in data.type.unique()
                            ],
                            value=sorted(data.type.unique())[0],
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Zakres dat", className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            display_format="YYYY-MM-DD",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"locale": "pl"},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"locale": "pl"},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    [
        Output("price-chart", "figure"),
        Output("volume-chart", "figure")
    ],
    [
        Input("shop-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(shop, avocado_type, start_date, end_date):
    mask = (
        (data.shop == shop)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {
                "text": "Średnia cena",
            },
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "bar",
            },
        ],
        "layout": {
            "title": {"text": "Sprzedaż",
            },
        },
    }
    return price_chart_figure, volume_chart_figure


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5555", debug=debug)

