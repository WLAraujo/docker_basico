# Código usado para criar uma API simples que nos permita usar nosso modelo como serviço

# Importações
from flask import Flask, request
import pickle
from numpy import array2string

# Modelo pickled
model_path = "rf-model.pkl"

# Realizando unpickle
with open(model_path, "rb") as file:
    unpickled_rf = pickle.load(file)

# Definindo o app
app = Flask(__name__)


# Usando um decorator para definir os atributo de entrada necessário 
@app.route("/score", methods=["POST", "GET"])
def predict_species():
    # Criação de lista para adicionar inputs
    flower = []
    flower.append(request.args.get("petal_length"))
    flower.append(request.args.get("petal_width"))
    flower.append(request.args.get("sepal_length"))
    flower.append(request.args.get("sepal_width"))

    # Retornando a predição
    print(unpickled_rf.predict([flower]))
    return array2string(unpickled_rf.predict([flower]))


# Rodar o app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")
    
# Requisição da API após rodar o código
# http://localhost:5001/score?petal_length=5.0&petal_width=2.0&sepal_length=3.5&sepal_width=1.0