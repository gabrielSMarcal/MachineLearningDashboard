from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)


app.layout = html.Div([
    # input de idade
    html.Label('Idade'),
    dcc.Input(id='input-idade', type='number', placeholder='Idade', value=0, min=0, max=120, step=1),
    # botão de submeter
    html.Button('Submeter', id='botao-submeter', n_clicks=0),
    # output de meses
    html.Div(id='output-meses')
])

@app.callback(
    Output('output-meses', 'children'),
    Input('botao-submeter', 'n_clicks'),
    State('input-idade', 'value'),
    prevent_initial_call=True
)

def calcula_meses(n_clicks, idade):
    if n_clicks == 0 or idade is None:
        return ''
    return idade * 12

app.run(debug=True)
