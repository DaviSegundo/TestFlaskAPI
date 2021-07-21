from flask import Flask, jsonify, request

api = Flask(__name__)

modelos = [
    {
        'nome' : 'AlexNet',
        'descricao' : '‘Modelo de CNN para classificação de imagens. Possui uma estrutura complexa com milhões de parâmetros, o que requer um volume imenso de dados para treinamento.'
    },
    {
       'nome' : 'VGGNet',
       'descricao' : 'Modelo de IA' 
    }
]

@api.route('/modelo', methods=['GET'])
def index():
    return jsonify(modelos), 200

@api.route('/modelo/<string:nome>', methods=['GET'])
def info(nome):
    modelo_nome = [modelo for modelo in modelos if modelo['nome'] == nome]
    return jsonify(modelo_nome), 200

@api.route('/modelo', methods=['POST'])
def adicionar():
    dados = request.get_json()
    modelos.append(dados)
    return jsonify(dados), 201
