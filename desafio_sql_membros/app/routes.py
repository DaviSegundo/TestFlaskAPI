from app import app
from app import db
from app.models import Projeto, Modelo, Membro
from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///app.db', echo = True)
Session = sessionmaker(bind = engine, autoflush=False)
session = Session()

@app.teardown_request
def remove_session(ex=None):
    session.close()

@app.route('/')
def inicio():
    return render_template('inicio.html')

'''
Parte sobre as informações do Modelo
'''

@app.route('/modelo', methods=['GET'])
def index():
    modelos = session.query(Modelo).all()
    return render_template('modelo.html', modelos=modelos)

@app.route('/modelo/<string:nome>', methods=['GET'])
def info_modelo(nome):
    modelos = session.query(Modelo).filter(Modelo.nome==nome).first()
    return render_template('info_modelo.html', modelos=modelos)

'''
Parte sobre as informações do Projeto
'''

@app.route('/projeto', methods=['GET'])
def index2():
    projetos = session.query(Projeto).all()
    return render_template('projeto.html', projetos=projetos)

@app.route('/projeto/<string:nome>', methods=['GET'])
def info_projeto(nome):
    projetos = session.query(Projeto).filter(Projeto.nome==nome).first()
    modelos = session.query(Modelo).filter(Modelo.projeto_nome==projetos.nome)
    return render_template('info_projeto.html', projetos=projetos, modelos=modelos)

'''
Parte sobre as informações do Membro
'''

@app.route('/membros', methods=['GET'])
def index3():
    membros = session.query(Membro).all()
    return render_template('membro.html', membros=membros)

@app.route('/membro/<string:nome>', methods=['GET'])
def info_membro(nome):
    membros = session.query(Membro).filter(Membro.nome==nome).first()
    return render_template('info_membro.html', membros=membros)

'''
Parte sobre POST de cada entidade
'''

@app.route('/modelo', methods=['POST'])
def adicionar_modelo():
    dados = request.get_json()
    nome = dados['nome']
    descricao = dados['descricao']
    projeto = dados['projeto']
    area_aplicacao = dados['area_aplicacao']
    p = session.query(Projeto).filter(Projeto.nome==projeto).first()
    if p is None:
        return 'Projeto não existente!'
    m = Modelo(nome=nome, descricao=descricao, area_aplicacao=area_aplicacao, pertence=p)
    local = db.session.merge(m)
    db.session.add(local)
    db.session.commit()
    return (dados), 201

@app.route('/projeto', methods=['POST'])
def adicionar_projeto():
    dados = request.get_json()
    nome = dados['nome']
    descricao = dados['descricao']
    if nome == '' or descricao == '':
        return 'Faltam informações para colocar!'
    p = Projeto(nome=nome, descricao=descricao)
    db.session.add(p)
    db.session.commit()
    return (dados), 201

@app.route('/membro', methods=['POST'])
def adicionar_membro():
    dados = request.get_json()
    nome = dados['nome']
    linguagem = dados['linguagem']
    m = Membro(nome=nome, linguagem=linguagem)
    db.session.add(m)
    db.session.commit()
    return (dados), 201
