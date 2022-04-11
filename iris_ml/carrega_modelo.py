# Importação do pickle
import pickle

# Caminho do modelo
model_path = 'rf-model.pkl'

# Realizando unpickle
with open(model_path, 'rb') as file:
    unpickled_rf = pickle.load(file)

# Vetor de teste do modelo
X_example = [[5.0, 2.0, 3.5, 1.0]]

# Rodando o modelo e printando o resultado
y_example = unpickled_rf.predict(X_example)
print(y_example)