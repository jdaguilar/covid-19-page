import plotly.graph_objs as go


def get_custom_indicator(value, delta=None):

    figure = go.Indicator(
        mode="number+delta",
        value=value,
        number={'valueformat': "000,000,000","font":{'size':40}},
        delta={
            "reference": delta,
            "valueformat": "000,000,000",
        },
    )

    return figure


def get_custom_pie_chart(labels,values):

    figure = go.Pie(
        labels=labels,
        values=values,
        hole=.5
    )

    return figure


def get_custom_histogram_chart(data,start,end,size,legend):

    figure = go.Histogram(
        x=data,
        histnorm='percent',
        name=legend,
        xbins=dict( # bins used for histogram
            start=start,
            end=end,
            size=size
        ),
        # marker_color='#EB89B5',
        # opacity=0.75
    )

    return figure


def get_custom_line_graph(
    x_data,
    y_data,
    legend=None,
    color=None
):

    figure = go.Scatter(
        x=x_data,
        y=y_data,
        name=legend,
        line=dict(color=color)
    )

    return figure


def get_custom_bar_chart(x_data,y_data,color=None,orientation=None):

    figure = go.Bar(
        x=x_data,
        y=y_data,
        marker_color=color,
        orientation=orientation,
    )

    return figure


def get_custom_map_chart(geojson, locations, z, text=None):

    figure = go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        z=z,
        colorscale='Blues',
        text=text,
        hoverinfo="text + z",
    )

    return figure
