# Third
from flask_marshmallow import Marshmallow

# Apps
from apps.users import models

ma = Marshmallow()


def configure_ma(app):
    ma.init_app(app)


class UserRegistrationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.UserMixin
        include_fk = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        include_fk = True
