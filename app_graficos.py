from dash import Dash, html

from utils import div_histograma, div_boxplot

app = Dash(__name__)
app.layout = html.Div([
    html.H1('Análise de dados do UCI Repository Heart Disease'),
    div_histograma,
    div_boxplot
])

# Exemplo de como adicionar mais componentes dinamicamente
# app.layout.children.append(div_boxplot)

app.run(debug=True)