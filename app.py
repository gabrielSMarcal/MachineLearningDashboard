from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__, external_stylesheets=['assets/main.css'])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Nav([
        dcc.Link('Gráficos', href='/graficos'),
        dcc.Link('Formulário', href='/formulario')
    ]),
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