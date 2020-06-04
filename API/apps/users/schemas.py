from flask_marshmallow import Marshmallow
from marshmallow.fields import Email, Str, Integer
from apps.users import models


ma = Marshmallow()


def configure_ma(app):
    ma.init_app(app)


class UserRegistrationSchema(ma.Schema):
    class Meta:
        full_name = Str(required=True)
        username = Str(required=True)
        email = Email(required=True)
        password = Str(required=True)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = models.User
        role = Integer(required=True)
        include_fk = True
