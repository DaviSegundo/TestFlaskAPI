import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO modelos (title, content) VALUES (?, ?)",
            ('AlexNet', 'Modelo de CNN para classificação de imagens. Possui uma estrutura complexa com milhões de parâmetros, o que requer um volume imenso de dados para treinamento.')
            )

connection.commit()
connection.close()
