from app import db

class Projeto(db.Model):
    id = db.Column(db.Integer)
    nome = db.Column(db.String(64), primary_key=True)
    membros = db.Column(db.String(500))
    modelos = db.relationship('Modelo', backref='pertence', lazy='dynamic')

    def __repr__(self):
        return '<Projeto {}>'.format(self.nome)


class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    descricao = db.Column(db.String(500), index=True, unique=True)
    area_aplicacao = db.Column(db.String(128))
    projeto_nome = db.Column(db.String(64), db.ForeignKey('projeto.nome'))

    def __repr__(self):
        return '<Modelo {}>'.format(self.nome)

#####