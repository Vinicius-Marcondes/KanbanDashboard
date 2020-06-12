# Python
from os import getenv
from datetime import timedelta


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or '69bb837b-44c0-443d-bc8b-294f91ccffec'
    APP_PORT = int(getenv('APP_PORT')) or 5000
    DEBUG = eval(getenv('DEBUG').title()) or True
    SQLALCHEMY_DATABASE_URI = getenv('POSTGRES_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(getenv('JWT_ACCESS_TOKEN_EXPIRES')))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(getenv('JWT_REFRESH_TOKEN_EXPIRES')))


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv('POSTGRES_URI_TEST')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
