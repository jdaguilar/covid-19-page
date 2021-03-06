import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html

from pages import (
    overview,
    historical,
    distribution
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-covid/historical":
        return historical.create_layout(app)
    elif pathname == "/dash-covid/distribution":
        return distribution.create_layout(app)
    else:
        return overview.create_layout(app)


if __name__ == '__main__':
    app.run_server(debug=True)
