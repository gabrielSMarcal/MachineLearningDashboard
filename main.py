from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
  
# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# metadata 
# print(heart_disease.metadata) 
  
# variable information 
# print(heart_disease.variables)

dados = heart_disease.data.features
# print(dados.head())

# plt.hist(dados['age'], bins=30, edgecolor='black')
# plt.title('Distribuição de Idade')
# plt.xlabel('Idade')
# plt.ylabel('Frequência')
# plt.show()

# print(1 * (heart_disease.data.targets > 0))

dados['doenca'] = 1 * (heart_disease.data.targets > 0)
# print(dados.head())

# sns.boxplot(y='age', x='doenca', data=dados, hue='doenca')
# plt.title('Idade por diagnóstico de Doença Cardíaca')
# plt.xlabel('Doença Cardíaca (0 = Não, 1 = Sim)')
# plt.ylabel('Idade')
# plt.show()

fig = px.histogram(dados, x='age', nbins=30)
fig.update_layout(
    title='Distribuição de Idade',
    xaxis_title='Idade',
    yaxis_title='Frequência')
fig.show()
