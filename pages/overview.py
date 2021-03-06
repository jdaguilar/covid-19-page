import json

import dash_html_components as html
from decouple import config
from urllib.request import urlopen

from data import get_total_casos, get_total_recuperados, get_total_fallecidos, \
    get_total_casos_activos, get_distribucion_por_departamento
from lib import get_indicator_card, get_bar_chart, get_map_chart
from utils import Header


token = config('MAPBOX_TOKEN')
geojson_url = 'https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json' 

with urlopen(geojson_url) as response:
    counties = json.load(response)

for loc in counties['features']:
    loc['id'] = loc['properties']['DPTO']


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # class "sub_page"
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [   # Product Summary
                            html.Div(
                                [
                                    html.H5("Panorama de casos COVID-19"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                        El siguiente es un dashboard basado en los datos y visualizaciones de la \
                                        página de Instituto Nacional de Salud (INS), hecha utilizando plotly Dash. \
                                        Para mas infomación: https://www.ins.gov.co/Noticias/Paginas/Coronavirus.aspx \
                                        ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Casos Confirmados"], className="subtitle padded"
                                    ),
                                    get_indicator_card(
                                        "graph-2",
                                        get_total_casos()
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Casos activos",
                                        className="subtitle padded",
                                    ),
                                    get_indicator_card(
                                        "graph-3",
                                        get_total_casos_activos()
                                    )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Casos Recuperados",
                                        className="subtitle padded",
                                    ),
                                    get_indicator_card(
                                        "graph-4",
                                        get_total_recuperados()
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Casos Fallecidos",
                                        className="subtitle padded",
                                    ),
                                    get_indicator_card(
                                        "graph-5",
                                        get_total_fallecidos()
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Casos por Departamento",
                                        className="subtitle padded",
                                    ),
                                    get_bar_chart(
                                        id="bar-graph-dep",
                                        data=get_distribucion_por_departamento(),
                                        x_col="nombre",
                                        y_col="cantidad",
                                        color="red",
                                        # orientation="v",
                                        # categoryorder="category ascending",
                                    ),
                                ],
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Mapa de casos",
                                        className="subtitle padded",
                                    ),
                                    get_map_chart(
                                        id="map-chart-dept",
                                        df=get_distribucion_por_departamento(),
                                        geojson=counties,
                                        locations="codigo",
                                        z="cantidad",
                                        text="nombre",
                                        token=token,
                                    )
                                ],
                            ),
                        ],
                        className="row ",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )