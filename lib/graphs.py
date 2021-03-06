import dash_core_components as dcc
import plotly.graph_objs as go

from lib.custom_figure import get_custom_bar_chart, get_custom_indicator, get_custom_pie_chart, \
    get_custom_histogram_chart, get_custom_line_graph, get_custom_map_chart
from lib.custom_layout import get_card_custom_layout, get_histogram_custom_layout, \
    get_bar_chart_custom_layout, get_map_chart_custom_layout


def get_indicator_card(id, value):

    graph = dcc.Graph(
        id=id,
        figure = {
            "data": [
                get_custom_indicator(value),
            ],
            "layout": get_card_custom_layout()
        }
    )

    return graph


def get_donut_chart(id, labels, values):

    graph = dcc.Graph(
        id=id,
        figure = {
            "data": [
                get_custom_pie_chart(labels, values)
            ],
            # "layout": go.Layout(
            #     autosize=True,
            #     font={"family": "Arial", "size": 10},
            #     height=80,
            #     width=170,
            #     margin={
            #         "r": 20,
            #         "t": 20,
            #         "b": 20,
            #         "l": 20,
            #     },
            # ),
        }
    )

    return graph


def get_histogram_chart(id, x, y, start, end, size):

    graph = dcc.Graph(
        id=id,
        figure = {
            "data": [
                get_custom_histogram_chart(x, y, start, end, size, "Edad"),
            ],
            "layout": get_histogram_custom_layout()
        }
    )

    return graph


def get_line_chart(id, datalist, x_col, y_col):

    line_graph = []

    for data,legend,color in datalist:
        line_graph.append(
            get_custom_line_graph(
                x_data=data[x_col],
                y_data=data[y_col],
                legend=legend,
                color=color,
            )
        )

    graph = dcc.Graph(
        id=id,
        figure = {
            "data": line_graph,
            # "layout": get_card_custom_layout()
        }
    )

    return graph


def get_bar_chart(id,data,x_col,y_col,color=None,orientation=None,categoryorder=None):

    graph = dcc.Graph(
        id=id,
        figure = {
            "data": [
                get_custom_bar_chart(data[x_col],data[y_col],color,orientation),
            ],
            "layout": get_bar_chart_custom_layout(categoryorder)
        }
    )

    return graph


def get_map_chart(id,df,geojson,locations,z,text,token):
    
    graph = dcc.Graph(
        id=id,
        figure = {
            "data": [
                get_custom_map_chart(
                    geojson=geojson,
                    locations=df[locations],
                    z=df[z],
                    text=df[text],
                )
            ],
            "layout": get_map_chart_custom_layout(token)
        }
    )

    return graph