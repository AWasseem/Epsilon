# Import packages
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import os


# Initialize the app - incorporate a Dash Bootstrap theme
# suppress_callback_exceptions=True # to avoid callback exceptions durin initial load
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css, dbc.icons.FONT_AWESOME],
    use_pages=True,
    suppress_callback_exceptions=True,
)
#used for WSGI for flask run
server = app.server
# Register the main page
dash.register_page(__name__, name="Home", path="/")

# Load the data
file_path = os.path.join(
    os.getcwd(),
    "GitHubProjects",
    "Mid Project",
    "Dash",
    "Train_cleaned.csv",
)

df = pd.read_csv(file_path)
dash_table_content = dash_table.DataTable(
    data=df.to_dict("records"),
    page_size=12,
    style_cell={"textAlign": "left"},
    style_as_list_view=True,
    style_table={"overflowX": "auto"},
)





Page_header_style = {"textAlign": "center"}

color_mode_switch = html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch(
            id="switch", value=True, className="d-inline-block ms-1", persistence=True
        ),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)


# App layout
app.layout = dbc.Container(
    children=[
        color_mode_switch,
        dbc.Row(
            dbc.Col(
                html.H1(children="U.S Income Exploratory ", style=Page_header_style),
                width=12,
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.NavLink(
                                    f"{page['name']}",
                                    href=page["relative_path"],
                                )
                            ]
                        )
                        for page in dash.page_registry.values()
                    ],
                    width=2,
                ),
                dbc.Col(
                    ["This data set represent income of U.S earning below or above $50,000 ",dash_table_content, dash.page_container],
                    width=10,
                ),
            ]
        ),
    ],
    fluid=True,
    className="dbc",
)

app.clientside_callback(
    """
    (switchOn) => {
        document.documentElement.setAttribute("data-bs-theme", switchOn ? "light" : "dark");
        return window.dash_clientside.no_update;
    }
    """,
    Output("switch", "value"),  # Ensuring this updates the `value` or other property
    Input("switch", "value"),
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
