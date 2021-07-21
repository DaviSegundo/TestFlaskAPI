import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_mail import Mail, Message

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_modelo(modelo_title):
    conn = get_db_connection()
    modelo = conn.execute('SELECT * FROM modelos WHERE title = ?',
                        (modelo_title,)).fetchone()
    conn.close()
    if modelo is None:
        abort(404)
    return modelo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'testedeemailflask@gmail.com',
	MAIL_PASSWORD = 'testedalead'
)
mail = Mail(app)


@app.route('/modelo')
def modelo():
    conn = get_db_connection()
    modelos = conn.execute('SELECT * FROM modelos').fetchall()
    conn.close()
    return render_template('modelo.html', modelos=modelos)

@app.route('/modelo/<string:modelo_title>')
def info(modelo_title):
    modelo = get_modelo(modelo_title)
    return render_template('info.html', modelo=modelo)

@app.route('/modelo/<string:modelo_title>/info_mail', methods=('GET', 'POST'))
def info_mail(modelo_title):  
    modelo = get_modelo(modelo_title)
    if request.method == 'POST':
        email = request.form['email']

        if not email:
            flash('Endereço de Email é necessário!')
        else:
            msg= Message('Send Mail Tutorial',
                sender = 'testedeemailflask@gmail.com',
                recipients = [email]
            )
            msg.body = 'Yo!\nHave you aaaaaa kekw'
            mail.send(msg)
            return 'Mail sent!'
    
    return render_template('info_mailv2.html')

@app.route('/modelo/criar_modelo', methods=('GET', 'POST'))
def criar():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Nome do Modelo é necessário!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO modelos (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('modelo'))
    return render_template('criar.html')

@app.route('/modelo/<string:modelo_title>/editar', methods=('GET', 'POST'))
def editar(modelo_title):
    modelo = get_modelo(modelo_title)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Nome do Modelo é necessário!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE modelos SET title = ?, content = ?'
                         ' WHERE title = ?',
                         (title, content, modelo_title))
            conn.commit()
            conn.close()
            return redirect(url_for('modelo'))

    return render_template('editar.html', modelo=modelo)

@app.route('/modelo/<string:modelo_title>/deletar', methods=('POST',))
def deletar(modelo_title):
    modelo = get_modelo(modelo_title)
    conn = get_db_connection()
    conn.execute('DELETE FROM modelos WHERE title = ?', (modelo_title,))
    conn.commit()
    conn.close()
    flash('"{}" deletado com sucesso!'.format(modelo['title']))
    return redirect(url_for('modelo'))