import plotly.graph_objs as go


def get_custom_indicator(value):

    figure = go.Indicator(
        mode="number",
        value=value,
        number={'valueformat': "000,000,000"}
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