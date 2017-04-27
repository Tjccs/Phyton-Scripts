import sqlite3
from flask import g, Blueprint


dbHandler = Blueprint('dbHandler', __name__, template_folder='servidor')

with dbHandler.app_context():
    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db


@dbHandler.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
