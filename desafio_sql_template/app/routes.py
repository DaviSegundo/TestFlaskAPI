from app import app
from app import db
from app.models import Projeto, Modelo
from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from jsonschema import validate

projeto_schema = {
    "title": "Projeto",
    "type": "object",
    "required": ["nome", "membros"],
    "properties":{
        "nome": {"type": "string"},
        "membros": {"type": "string"}
    }
}

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/modelo', methods=['GET'])
def index():
    modelos = Modelo.query.all()
    return render_template('modelo.html', modelos=modelos)

@app.route('/modelo/<string:nome>', methods=['GET'])
def info_modelo(nome):
    modelos = Modelo.query.filter(Modelo.nome==nome).first()
    return render_template('info_modelo.html', modelos=modelos)

@app.route('/projeto', methods=['GET'])
def index2():
    projetos = Projeto.query.all()
    return render_template('projeto.html', projetos=projetos)

@app.route('/projeto/<string:nome>', methods=['GET'])
def info_projeto(nome):
    projetos = Projeto.query.filter(Projeto.nome==nome).first()
    modelos = Modelo.query.filter(Modelo.projeto_nome==projetos.nome)
    return render_template('info_projeto.html', projetos=projetos, modelos=modelos)

@app.route('/modelo', methods=['POST'])
def adicionar_modelo():
    dados = request.get_json()
    nome = dados['nome']
    descricao = dados['descricao']
    projeto = dados['projeto']
    area_aplicacao = dados['area_aplicacao']
    p = Projeto.query.filter(Projeto.nome==projeto).first()
    if p is None:
        return 'Projeto não existente!'
    m = Modelo(nome=nome, descricao=descricao, area_aplicacao=area_aplicacao, pertence=p)
    db.session.add(m)
    db.session.commit()
    return (dados), 201

@app.route('/projeto', methods=['POST'])
def adicionar_projeto():
    dados = request.get_json()
    if validate(dados, projeto_schema) is not None:
        return 'erro!'
    nome = dados['nome']
    membros = dados['membros']
    #p = Projeto(nome=nome, membros=membros)
    #db.session.add(p)
    #db.session.commit()
    return (dados), 201
