from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
ma = Marshmallow()


class LoginSchema(ma.SQLAlchemySchema):
    email = fields.Str()
    username = fields.Str()
    password = fields.Str(required=True)
