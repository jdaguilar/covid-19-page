import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go

from data import *
from lib import get_donut_chart, get_bar_chart
from utils import Header


distr_genero_df = get_distribucion_por_genero()


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
                                        ["Distribución por género"], className="subtitle padded"
                                    ),
                                    get_donut_chart(
                                        id="donut-graph",
                                        labels=distr_genero_df["Sexo"],
                                        values=distr_genero_df["cantidad"]
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Distribución por Edad"], className="subtitle padded"
                                    ),
                                    get_bar_chart(
                                        id="histogram-graph",
                                        data=get_edades(),
                                        x_col="edad",
                                        y_col="cantidad",
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

                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )