from app import db
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

participacao_table = Table('participacao', Base.metadata,
    db.Column('projeto_nome', db.String(64), db.ForeignKey('projeto.nome'), primary_key=True),
    db.Column('membro_nome', db.String(64), db.ForeignKey('membro.nome'), primary_key=True)
)

class Projeto(Base):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer)
    nome = db.Column(db.String(64), primary_key=True)
    descricao = db.Column(db.String(500), index=True, unique=True)
    #membros = db.Column(db.String(500))
    modelos = db.relationship('Modelo', backref='pertence')
    membros = db.relationship('Membro', secondary=participacao_table, lazy='subquery', backref=db.backref('membros', lazy=True))

    def __repr__(self):
        return '<Projeto {}>'.format(self.nome)

class Membro(Base):
    __tablename__ = 'membro'
    id = db.Column(db.Integer)
    nome = db.Column(db.String(64), primary_key=True)
    linguagem = db.Column(db.String(128))
    
    def __repr__(self):
        return 'Membro {}>'.format(self.nome)

class Modelo(Base):
    __tablename__ = 'modelo'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    descricao = db.Column(db.String(500), index=True, unique=True)
    area_aplicacao = db.Column(db.String(128))
    projeto_nome = db.Column(db.String(64), db.ForeignKey('projeto.nome'))

    def __repr__(self):
        return '<Modelo {}>'.format(self.nome)






###########