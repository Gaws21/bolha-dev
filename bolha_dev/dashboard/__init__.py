"""Instantiate a Dash app."""
import dash
from dash import html
from flask import Flask
from .layout import html_layout
from .dcc_graphs import div_count_posicao, div_c2, div_c3

def init_dashboard(app: Flask):
    """
    Create a Plotly Dash dashboard within a running Flask app.

    :param Flask app: Top-level Flask application.
    """
    dash_module = dash.Dash(
        server=app,
        routes_pathname_prefix="/dashboard/",
        external_stylesheets=[
            "/static/css/output.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Custom HTML layout
    dash_module.index_string = html_layout

    letra_b = html.H1(
    children=['Bolha dev'],
)
    
    grafico_1 = html.Div(
        children=['grafico-1'],
        className="m-2 gap-1 drop-shadow-lg bg-white flex items-center rounded-2xl"
    )

    grafico_2_filho = html.Div(
        children=['indicador'],
        className="m-2 gap-1 drop-shadow-lg bg-white flex items-center rounded-2xl"
    )

    grafico_2 = html.Div(
        children=[grafico_2_filho, grafico_2_filho, grafico_2_filho],
        className="m-2 gap-1 flex flex-col items-center"
    )

    tabela_historica = html.Div(
        children=['tabela-historica'],
        className="m-2 gap-1 drop-shadow-lg bg-white flex items-center rounded-2xl"
    )

    main_1 =  html.Div(
        children=[
            div_count_posicao,
            div_c2,
            div_c3
        ],
        id="dash-container",
        className="grid grid-cols-3 gap-2"
    )


    # Create Layout
    dash_module.layout = html.Div(
        children=[
           main_1,
           tabela_historica
        ],
    )
    return dash_module.server
