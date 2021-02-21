import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(src=app.get_asset_url("virus.jpg"),className="logo"),
                    # html.A(
                    #     html.Button("Learn More", id="learn-more-button"),
                    #     href="https://plot.ly/dash/pricing/",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Dashboard COVID-19")],
                        className="main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Panorama general",
                href="/dash-covid/overview",
                className="tab first",
            ),
            dcc.Link(
                "Historico de casos",
                href="/dash-covid/historical",
                className="tab",
            ),
            dcc.Link(
                "Distribución de casos",
                href="/dash-covid/distribution",
                className="tab",
            ),
            # dcc.Link(
            #     "Fees & Minimums", href="/dash-financial-report/fees", className="tab"
            # ),
            # dcc.Link(
            #     "Distributions",
            #     href="/dash-financial-report/distributions",
            #     className="tab",
            # ),
            # dcc.Link(
            #     "News & Reviews",
            #     href="/dash-financial-report/news-and-reviews",
            #     className="tab",
            # ),
        ],
        className="row all-tabs",
    )
    return menu

def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table