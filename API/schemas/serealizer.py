from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import auto_field
from API.models.model import Person

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Person
        load_instance = True

    id = auto_field()
    name = auto_field()
    email = auto_field()

