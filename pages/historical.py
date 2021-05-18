import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go

from data import get_acumulado_fallecidos,get_acumulado_recuperados,get_total_acumulado

from lib import get_line_chart, get_bar_chart
from utils import Header


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # class "sub_page"
            html.Div(
                [
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Acumulado de casos"], className="subtitle padded"
                                    ),
                                    get_line_chart(
                                        id="histo-graph",
                                        datalist=[
                                            (get_total_acumulado(),"Total","blue"),
                                            (get_acumulado_fallecidos(),"Fallecido","red"),
                                            (get_acumulado_recuperados(),"Recuperado","green")
                                        ],
                                        x_col='fecha',
                                        y_col='acumulado'
                                    ),
                                ],
                                # className="six columns",
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
                                        "Fallecidos por día",
                                        className="subtitle padded",
                                    ),
                                    get_bar_chart(
                                        id="bar-graph",
                                        data=get_acumulado_fallecidos(),
                                        x_col="fecha",
                                        y_col="cantidad",
                                        color="red",
                                        categoryorder='total descending',
                                    ),
                                ],
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.H6(
                                ["Casos confirmados por día"],className="subtitle padded"
                            ),
                            get_bar_chart(
                                id="bar-graph2",
                                data=get_total_acumulado(),
                                x_col="fecha",
                                y_col="cantidad",
                            ),
                        ]
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )