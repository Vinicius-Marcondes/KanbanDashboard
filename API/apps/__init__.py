from flask import Flask
from flask_migrate import Migrate
from config import config
from .api import configure_api
from .db import configure_db
from .jwt import configure_jwt
from .users.schemas import configure_ma


def create_app(config_name):
    app = Flask('API')
    app.config.from_object(config[config_name])

    # Initialize db configs
    configure_db(app)
    # Initialize marshmallow_sqlalchemy
    configure_ma(app)
    # Enable database migration
    Migrate(app, app.db)
    # Config JWT
    configure_jwt(app)
    # Initialize api config
    configure_api(app)

    return app
