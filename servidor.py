"""
Routing module

@author: grupo28
"""

# import area ##################################################################
from flask import Flask, g, request
import os
import sqlite3
################################################################################

app = Flask(__name__)
app.config.from_object(__name__)

DATABASE = os.path.join(app.root_path, 'database.db')
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database.db')))


################################################################################
# Database handler
# with app.app_context():
# def get_db():
# db = getattr(g, '_database', None)
# if db is None:
# db = g._database = sqlite3.connect(DATABASE)
# db.row_factory = sqlite3.Row
# return db

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.before_first_request
def setup_database():
    query = 'INSERT INTO rates (id, designacao, sigla) VALUES (1,"Mau","M"), (2, "Mais ou menos", "MM"), (3, "Suficiente", "S"), (4, "Bom", "B"), (5, "Muito bom", "MB");'
    cur = connect_db().execute(query)
    cur.close()


# @app.teardown_appcontext
# def close_connection(exception):
# db = getattr(g, '_database', None)
# if db is not None:
# db.close()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# @app.errorhandler(customerror)
# def custom_error(e):
#    return 'METHOD NOT ALLOWED'


################################################################################
# Database Queries


# Query function
def query_db(query, args=(), one=False):
    cur = connect_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# Add user to the db
def add(id, nome, username, password, id_banda, ano, genero):
    db = get_db()
    if 'ADD USER':
        db.execute('INSERT INTO utilizadores (id, nome, username, password) VALUES (?,?,?,?)', (id, nome, username, password))
    if 'ADD BAND':
        db.execute('INSERT INTO bandas (nome, ano, genero) VALUES (?,?,?)', (nome, ano, genero))
    if 'ADD ALBUM':
        db.execute('INSERT INTO album (id_banda, nome, ano) VALUES (?,?,?)', (id_banda, nome, ano))
    db.commit()
    return 'ADD completed...'


# Show one user
def show(id):
    user = query_db('SELECT * FROM utilizadores WHERE id = ?', (id), one=True)
    if user is None:
        return 'No such user'
    else:
        return user


# Show all users
def show_all():
    if 'SHOW ALL USERS':
        for user in query_db('SELECT * FROM utilizadores'):
            print(user['id'], user['username'], user['nome'])
    if 'SHOW ALL BANDAS':
        for band in query_db('SELECT * FROM bandas'):
            print(band['nome'], band['ano'], band['genero'])
    if 'SHOW ALL ALBUM':
        for album in query_db('SELECT * FROM album'):
            print(album['id_banda'], album['nome'], album['ano'])


# Remove all users
def remove_all_users():
    g.db.execute('DELETE * FROM utilizadores')
    g.db.commit()
    return 'Removed all users'


################################################################################
# Set users page and main page for the application
@app.route('/')
def index():
    res = 'SUPPORTED OPERATIONS: ADD, REMOVE, SHOW, UPDATE'
    ult = '"\n" PAGES: /utilizadores/, /bandas/, /albuns/'
    adoo = '"\n" ROUTING: /page/operation'
    resultado = res+ult+adoo
    return resultado


@app.route('/utilizadores/add', methods=['POST'])
def user_add():
    if request.method == 'POST':
        add()
        return 'RESPONSE'
    else:
        return 'Method not allowed'


# Set bandas page route
@app.route('/bandas')
def bands_page():
    return "Bands!!"


# Set albuns page route
@app.route('/albuns')
def albuns_page():
    return "ALBUNS!!"


if __name__ == "__main__":
    app.run()
