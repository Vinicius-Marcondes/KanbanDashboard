from flask import Flask
from flask_migrate import Migrate
from API.models.model import configure as config_db
from API.schemas.serealizer import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from API.views.person import bp_person
    app.register_blueprint(bp_person)

    return app
