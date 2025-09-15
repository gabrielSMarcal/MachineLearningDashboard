from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div([
    html.H1('Previsão de doença cardíaca'),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label('Idade'),
                    dbc.Input(id='input-idade', type='number', placeholder='Digite sua idade'),
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Sexo biológico'),
                    dbc.Select(id='sexo', options=[
                        {'label': 'Masculino', 'value': '0'},
                        {'label': 'Feminino', 'value': '1'}
                    ],
                    )
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Tipo de dor no peito'),
                    dbc.Select(id='tipo-dor', options=[
                        {'label': 'Angina típica', 'value': '1'},
                        {'label': 'Angina atípica', 'value': '2'},
                        {'label': 'Não angina', 'value': '3'},
                        {'label': 'Angina assintomática', 'value': '4'}
                    ],
                    )
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Pressão arterial em repouso'),
                    dbc.Input(id='trestbps', type='number', placeholder='Digite sua pressão arterial em repouso'),
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Colesterol sérico (mg/dl)'),
                    dbc.Input(id='chol', type='number', placeholder='Digite seu colesterol sérico'),
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Glicemia em jejum'),
                    dbc.Select(id='fbs', options=[
                        {'label': 'Menor que 120 mg/dl', 'value': '0'},
                        {'label': 'Maior que 120 mg/dl', 'value': '1'}
                    ],
                    )
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Eletrocardiografia em repouso'),
                    dbc.Select(id='restecg', options=[
                        {'label': 'Normal', 'value': '0'},
                        {'label': 'Anormalidade de ST-T', 'value': '1'},
                        {'label': 'Hipertrofia ventricular esquerda', 'value': '2'}
                    ],
                    )
                ], className='mb-3'),
                ]),
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label('Frequência cardíaca máxima atingida'),
                    dbc.Input(id='thalach', type='number', placeholder='Digite sua frequência cardíaca máxima atingida'),
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Angina induzida por exercício'),
                    dbc.Select(id='exang', options=[
                        {'label': 'Não', 'value': '0'},
                        {'label': 'Sim', 'value': '1'}
                    ],
                    )
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Depressão do segmento ST induzida por exercício'),
                    dbc.Input(id='oldpeak', type='number', placeholder='Digite o valor de oldpeak'),
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Inclinação do segmento ST'),
                    dbc.Select(id='slope', options=[
                        {'label': 'Ascendente', 'value': '1'},
                        {'label': 'Plana', 'value': '2'},
                        {'label': 'Descendente', 'value': '3'}
                    ],
                    )
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Número de vasos principais coloridos por fluoroscopia'),
                    dbc.Select(id='ca', options=[
                        {'label': '0', 'value': '0'},
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'}
                    ],
                    )
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Label('Cintilografia do miocárdio'),
                    dbc.Select(id='thal', options=[
                        {'label': 'Normal', 'value': '3'},
                        {'label': 'Defeito fixo', 'value': '6'},
                        {'label': 'Defeito reversível', 'value': '7'},
                    ]),
                ], className='mb-3'),
                dbc.CardGroup([
                    dbc.Button('Prever', id='botao-prever', color='primary')
                ], className='mb-3'),
        ])
    ])
    
        
    ])
])

app.run(debug=True)