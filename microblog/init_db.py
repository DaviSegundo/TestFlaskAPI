import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES(?, ?)",
('Praticando Flask', 'Fazendo Blog bonitinho'))

cur.execute("INSERT INTO posts (title, content) VALUES(?, ?)",
('Olha as coisas melhorando!', 'Agora vai hein!'))

connection.commit()
connection.close()