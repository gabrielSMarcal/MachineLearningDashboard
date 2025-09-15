from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=['assets/main.css', dbc.themes.FLATLY])

navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
        dbc.NavItem(dbc.NavLink("Início", href="/")),
    ],
    brand="Dashboard de Análise de Doença Cardíaca",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navegacao,
    html.Div(id='conteudo')
])

@app.callback(
    Output('conteudo', 'children'),
    [Input('url', 'pathname')]
)

def mostrar_pagina(pathname):
    if pathname== '/graficos':
        return html.P('Página de Gráficos')
    elif pathname == '/formulario':
        return html.P('Página de Formulário')
    return html.P('Página Inicial')

app.run(debug=True)