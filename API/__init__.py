from flask import Flask, url_for
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma
from markupsafe import escape


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .person import bp_person
    app.register_blueprint(bp_person)

    return app


# api = create_app()


# @api.route('/')
# def index():
#     return 'index'
#
#
# @api.route('/login')
# def login():
#     return 'login'
#
#
# @api.route('/user/<string:name>')
# def profile(name):
#     return '{}\'s profile'.format(escape(name))
#
#
# with api.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', name='Vinicius'))
