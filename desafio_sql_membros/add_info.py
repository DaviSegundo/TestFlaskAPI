from app import db
from app.models import Projeto, Modelo, Membro
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///app.db', echo = True)
Session = sessionmaker(bind = engine, autoflush=False)
session = Session()

pro = session.query(Projeto).first()
pro_all = session.query(Projeto).all()
mem_all = session.query(Membro).all()
mem = session.query(Membro).filter(Membro.nome=='Davi Segundo').first()

print('\n')
print(pro_all)
print(mem_all)
print('\n')

print('\n')
print(pro)
print(mem)
print('\n')


pro.membros.append(mem)
session.commit()

for k in pro.membros:
    print(k.nome)




