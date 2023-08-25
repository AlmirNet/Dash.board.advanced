from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import app
from components import dashboards, extratos
            
from globals import *

import sidebar


# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dcc.Store(id='store-receita', data=df_receitas.to_dict()),
    dcc.Store(id='store-despesa', data=df_despesas.to_dict()),
    dcc.Store(id='store-cat-receita', data=df_cat_receitas.to_dict()),
    dcc.Store(id='store-cat-despesa', data=df_cat_despesas.to_dict()),


    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10),
    ])

], fluid=True,)


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboard':
        return dashboards.layout
    if pathname == '/extratos':
        return extratos.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)