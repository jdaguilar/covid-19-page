import plotly.graph_objs as go


def get_card_custom_layout():

    layout = go.Layout(
        autosize=True,
        font={"family": "Arial", "size": 10},
        height=90,
        width=200,
        margin={
            "r": 7,
            "t": 7,
            "b": 7,
            "l": 7,
        },
    )

    return layout


def get_histogram_custom_layout():

    layout = go.Layout(
        # title_text='Sampled Results', # title of plot
        # xaxis_title_text='Value', # xaxis label
        # yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1 # gap between bars of the same location coordinates
    )

    return layout


def get_bar_chart_custom_layout(categoryorder=None):

    layout = go.Layout(
        yaxis={
            'categoryorder':categoryorder
        }
    )

    return layout


def get_map_chart_custom_layout(token):

    layout = go.Layout(
        mapbox_style="light",
        mapbox_accesstoken=token,
        mapbox_zoom=3,
        mapbox_center = {"lat": 4.570868, "lon": -74.2973328}
    )

    return layout