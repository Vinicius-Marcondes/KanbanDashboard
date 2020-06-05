from flask import current_app, request

# Third
from bcrypt import gensalt, hashpw
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

# Apps
from apps.messages import (
    MSG_EXCEPTION,
    MSG_NO_DATA,
    MSG_PASSWORD_DIDNT_MATCH,
    MSG_RESOURCE_CREATED
)
from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_invalid_data,
    resp_ok
)

# Local
from .models import User
from .schemas import UserRegistrationSchema, UserSchema
from .utils import check_password_in_singup


class SingUp(Resource):

    def post(self, *args, **kwargs):
        req_data = request.json or None
        data, errors, result = None, None, None
        password, confirm_password = None, None
        schema = UserSchema()

        if req_data is None:
            return resp_invalid_data('Users', {}, msg=MSG_NO_DATA)

        password = req_data.get('password')
        confirm_password = req_data.pop('confirm_password', None)

        if not check_password_in_singup(password, confirm_password):
            errors = {'password': MSG_PASSWORD_DIDNT_MATCH}
            return resp_invalid_data('Users', errors)

        try:
            data = schema.load(req_data)

        except ValidationError as err:
            return resp_invalid_data('Users', err.messages)

        password_hashed = hashpw(password.encode('utf-8'), gensalt(12))

        try:
            data.update({'password': password_hashed, 'email': (data['email'].lower())})
            current_app.db.session.add(User(**data))
            current_app.db.session.commit()

        except IntegrityError as err:
            return resp_already_exists('Users', err.orig)

        except ValidationError as err:
            return resp_exception('Users', msg=MSG_EXCEPTION, description=err.messages)

        except Exception as err:
            return resp_exception('Users', msg=err)

        schema = UserRegistrationSchema()
        result = schema.dump(data)

        return resp_ok('Users', MSG_RESOURCE_CREATED.format('User'), data=result)
