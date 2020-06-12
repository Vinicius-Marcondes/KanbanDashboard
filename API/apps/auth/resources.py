from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from bcrypt import checkpw
from apps.users.models import User
from apps.users.schemas import UserSchema
from apps.users.utils import get_user_by_email
from apps.messages import MSG_NO_DATA, MSG_TOKEN_CREATED
from apps.responses import resp_invalid_data, resp_not_allowed_user, resp_ok
from .schemas import LoginSchema


class AuthResource(Resource):
    def post(self, *args, **kwargs):
        """
        This method is used to login with the API
        """
        req_data = request.get_json() or None
        user = None
        login_schema = LoginSchema()
        schema = UserSchema

        if req_data is None:
            return resp_invalid_data('Users', {}, msg=MSG_NO_DATA)

        try:
            data = login_schema.load(req_data)
        except ValueError:
            return resp_invalid_data('Users', ValueError.__dict__)

        user = get_user_by_email(data.get('email'))

        if not isinstance(user, User):
            return user

        if not user.is_active:
            return resp_not_allowed_user('Auth')

        if checkpw(data.get('password').encode('utf-8'), user.password.encode('utf-8')):
            extras = {
                'token': create_access_token(identity=user.email),
                'refresh': create_refresh_token(identity=user.email)
            }

            result = schema.dump(user.__dict__)

            return resp_ok('Auth', MSG_TOKEN_CREATED, data=result, **extras)

        return resp_not_allowed_user('Auth')
