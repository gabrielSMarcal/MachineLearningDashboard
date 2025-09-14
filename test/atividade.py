from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from teste_de_dados import dados

# Atividade 1: Visualização de Dados
# fig = px.box(dados, x='doenca', y='chol', color='doenca',
#              labels={'doenca': 'Doença Cardíaca (0 = Não, 1 = Sim)', 'chol': 'Colesterol'})
# fig.update_layout(
#     title='Colesterol sérico vs Presença de Doença Cardíaca',
#     xaxis_title='Doença Cardíaca (0 = Não, 1 = Sim)',
#     yaxis_title='Colesterol sérico (mg/dl)'
# )
# fig.show()

fig = px.box(dados, x='doenca', y='trestbps', color='doenca',
             labels={'doenca': 'Doença Cardíaca (0 = Não, 1 = Sim)', 'trestbps': 'Pressão Arterial em Repouso'})
fig.update_layout(
    title='Pressão Arterial em Repouso vs Presença de Doença Cardíaca',
    xaxis_title='Doença Cardíaca (0 = Não, 1 = Sim)',
    yaxis_title='Pressão Arterial em Repouso (mm Hg)'
)
fig.show()