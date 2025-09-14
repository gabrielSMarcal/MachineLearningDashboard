from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados['doenca'] = 1 * (heart_disease.data.targets > 0)
# print(dados.head())

'''HISTOGRAMA E BOXPLOT'''
figura_histograma = px.histogram(
    dados, x='age',
    nbins=30,
    title='Distribuição da Idade'
)

figura_boxplot = px.box(
    dados,
    x='doenca',
    y='age',
    color='doenca',
    title='Idade por diagnóstico de Doença Cardíaca'
)

'''VARIÁVEIS PARA O LAYOUT DO DASH'''
div_histograma = html.Div([
        html.H2('Histograma de idades'),
        dcc.Graph(figure=figura_histograma)
    ])

div_boxplot = html.Div([
    html.H2('Boxplot de idades'),
    dcc.Graph(figure=figura_boxplot)
])