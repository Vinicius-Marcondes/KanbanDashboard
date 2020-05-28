from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Person

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class PersonSchema(ma.Schema):
    class Meta:
        model = Person
