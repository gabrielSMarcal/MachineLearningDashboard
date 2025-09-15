from dash import dcc, html
from ucimlrepo import fetch_ucirepo
import dash_bootstrap_components as dbc
import plotly.express as px

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados['doenca'] = 1 * (heart_disease.data.targets > 0)

standard = 'text-center mb-3 mt-3'

'''HISTOGRAMA E BOXPLOT'''
figura_histograma = px.histogram(
    dados, x='age',
    nbins=30,
    title='Distribuição da Idade'
)
figura_histograma.update_layout(title_x=0.5)

figura_boxplot = px.box(
    dados,
    x='doenca',
    y='age',
    color='doenca',
    title='Boxplot de idades'
)
figura_boxplot.update_layout(title_x=0.5)

'''VARIÁVEIS PARA O LAYOUT DO DASH'''
div_histograma = html.Div([
        dcc.Graph(figure=figura_histograma, className='mb-5')
    ])

div_boxplot = html.Div([
    dcc.Graph(figure=figura_boxplot, className='mb-5')
])

layout_grafico = html.Div([
    html.H1('Análise de dados do UCI Repository Heart Disease', className=standard),
    dbc.Container([
        dbc.Row([
            dbc.Col([div_histograma], md=6),
            dbc.Col([div_boxplot], md=6)
        ])
    ])
])