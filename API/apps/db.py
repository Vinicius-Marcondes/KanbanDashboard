# Third
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure_db(app):
    db.init_app(app)
    app.db = db
