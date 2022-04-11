# Importações e definições
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Seed para números aleatórios
seed_number = 123

# Carregar dataset de iris
from sklearn import datasets
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)


# Divisão treino e teste
test_proportion = 0.3
X_train, X_test, y_train, y_test = train_test_split(
    df[iris.feature_names],
    iris.target,
    test_size=test_proportion,
    stratify=iris.target,
    random_state=seed_number,
)

# Criação do objeto modelo
n_trees = 100
rf = RandomForestClassifier(
    n_estimators=n_trees, oob_score=True, random_state=seed_number
)

# Treino do modelo
rf.fit(X_train, y_train)

# Avaliação do modelo e apresentação do resultado
predicted = rf.predict(X_test)
accuracy = accuracy_score(y_test, predicted)
print(
    "Out-of-bag score estimate: {0:.3f}\n"
    "Mean accuracy score: {1:.3f}".format(rf.oob_score_, accuracy
    )
)

# Serialização do modelo
pickle_save = 'rf-model.pkl'
with open(pickle_save, 'wb') as file:
    pickle.dump(rf, file)