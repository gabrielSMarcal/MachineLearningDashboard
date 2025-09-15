from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo
import joblib
import xgboost as xgb

SEED = 432

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados['doenca'] = 1 * (heart_disease.data.targets > 0)

X = dados.drop(columns='doenca')
y = dados['doenca']

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=SEED,
    stratify=y
)

modelo = xgb.XGBClassifier(objective='binary:logistic')
modelo.fit(X_treino, y_treino)
predicoes = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, predicoes) * 100
# print(f'Acurácia: {acuracia:.2f}%') # Acurácia: 81.97%

joblib.dump(modelo, 'modelo_xgboost.pkl')

medianas = X.median()

joblib.dump(medianas, 'medianas.pkl')