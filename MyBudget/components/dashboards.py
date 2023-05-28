from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar

from app import app

card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin":"auto",
}

# =========  Layout  =========== #
layout = dbc.Col([
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    html.Legend('Saldo'),
                    html.H5('R$5400', id='p-saldo-dashboards', style={})
                ], style={'padding-left': '20px', 'padding-top': '10px'}),
                dbc.Card([
                    html.Div(className='fa fa-university')
                ])
            ])
        ])
    ])



# =========  Callbacks  =========== #
