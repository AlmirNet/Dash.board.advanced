import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Advanced Budget", className='text-primary'),
    html.P('By ALMIRNET', className='text-info'),
    html.Hr(),

    # Seção PERFIL --------------------------------
    dbc.Button(
        id='botao_avatar',
        children=html.Img(src='/assets/img_hom.png', id='avatar_change',alt='Avatar', className='perfil_avatar')
    ),

    # Seção NOVO -------------------------------------
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success',
                       id='open-novo-receita', children=['Receita'])
        ], width=6),

        dbc.Col([
            dbc.Button(color='danger', id='open-novo-despesa', children=['Despesa'])
        ], width=6),
    ]),

    # Modal Receita
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Adicionar receita")),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição'),
                    dbc.Input(placeholder='Ex.: dividendos da bolsa, herança...', id="txt-receita"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Data"),
                    dcc.DatePickerSingle(id='date-receitas',
                        min_date_allowed=date(2020, 1, 1),
                        max_date_allowed=date(2030, 12, 31),
                        date=datetime.today(),
                        style={"width": "100%"}
                    ),
                ], width=4),

                dbc.Col([
                    dbc.Label("Extra"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switches-input-receita',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Categoria da receita'),
                    dbc.Select(id='select_receita', options=[])
                ], width=4),
            ], style={'margin-top': '25px'})
        ])
    ], id='modal-novo-receita'),

    # Modal Despesa
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Adicionar despesa")),
        dbc.ModalBody([
    
        ])
    ], id='modal-novo-despesa'),

    # Seção NAV ------------------------------------
    html.Hr(),
    html.Nav([
        dbc.NavLink('Dashboard', href='/dashboards', active='exact'),
        dbc.NavLink('Extratos', href='/extratos', active='exact')
    ]),

    
],)



# ========================== Callbacks ====================== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
