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

from globals import *

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
                    dbc.Select(id='select_receita', 
                               options=[{'label': i, 'value': i} for i in cat_receita],
                               value=[])
                ], width=4),
            ], style={'margin-top': '25px'}),

            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn-sucess", id="add-category-receita", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-receita", style={}),
                            ], width=6),  
                            dbc.Col([
                                html.Legend('Excluir categoria', style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-receita',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categoria')
                ], flush=True, start_collapsed=True, id='accordion-receita'),

                html.Div(id='id_teste_receita', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Receitas", id="salva_receita", color="success"),
                    dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                ])

            ], style={'margin-top': '25px'}),
        ])
    ], style={"background-color": "rgba(17, 140, 79, 0.05)"}, 
    id="modal-novo-receita",
    size="lg",
    is_open=False,
    centered=True,
    backdrop=True),

    # Modal Despesa
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Adicionar despesa")),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição'),
                    dbc.Input(placeholder='Ex.: Alimentos,celular...', id="txt-despesa"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="$100.00", id="valor_despesa", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Data"),
                    dcc.DatePickerSingle(id='date-despesa',
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
                        id='switches-input-despesa',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Categoria da Despesa'),
                    dbc.Select(id='select_despesa',
                                options=[{'label': i, 'value': i} for i in cat_despesa],
                                value=cat_despesa[0])
                ], width=4),
            ], style={'margin-top': '25px'}),

            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn-sucess", id="add-category-despesa", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-despesa", style={}),
                            ], width=6),  
                            dbc.Col([
                                html.Legend('Excluir categoria', style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-despesa',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-despesa', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categoria')
                ], flush=True, start_collapsed=True, id='accordion-despesa'),

                html.Div(id='id_teste_despesa', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Despesa", id="salva_despesa", color="success"),
                    dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_receita", placement="left", trigger="click"),
                ])

            ], style={'margin-top': '25px'}),
    
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
    

@callbacks
