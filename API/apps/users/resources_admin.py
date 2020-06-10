from flask import request, current_app
from marshmallow import ValidationError
import re
from sqlalchemy.exc import NoReferencedColumnError, IntegrityError
from flask_restful import Resource
from apps.users.utils import get_user_by_id, exists_email_in_user, check_password_in_singup
from apps.messages import MSG_RESOURCE_FETCHED_PAGINATED, MSG_RESOURCE_FETCHED, MSG_NO_DATA, MSG_ALREADY_EXISTS, \
    MSG_RESOURCE_UPDATED, MSG_PASSWORD_DIDNT_MATCH, MSG_RESOURCE_DELETED
from apps.responses import resp_ok, resp_exception, resp_does_not_exist, resp_invalid_data, resp_already_exists

from .models import User
from .schemas import UserSchema, UserUpdateSchema


class AdminUserPageList(Resource):
    def get(self, page_id: int = 1) -> dict:
        """
        Lists the users from the db
        :param page_id: int
        :return: dict
        """

        schema = UserSchema(many=True)
        page_size = 10

        if 'page_size' in request.args:
            if int(request.args.get('page_size')) < 1:
                page_size = 10
            else:
                page_size = int(request.args.get('page_size'))

        try:
            users = User.query.paginate(page_id, page_size)

        except NoReferencedColumnError as err:
            return resp_exception('Users', description=err.__str__())

        except Exception as err:
            return resp_exception('Users', description=err.__str__())

        extras = {
            'page': users.page,
            'pages': users.pages,
            'total': users.total,
            'params': {'page_id': page_id,
                       'page_size': page_size}
        }

        result = schema.dump(users.items)

        return resp_ok('User', MSG_RESOURCE_FETCHED_PAGINATED.format('users'), data=result, **extras)


class AdminUserResource(Resource):
    def get(self, user_id: int) -> dict:

        try:
            query = get_user_by_id(user_id)
            result = UserSchema(many=True).dump(query)

        except Exception:
            return resp_does_not_exist('User', "user")

        return resp_ok('User', MSG_RESOURCE_FETCHED.format('User'), data=result)

    def put(self, user_id):
        result = None
        schema = UserSchema(many=True)
        update_schema = UserUpdateSchema()
        req_data = request.json or None
        email = None

        if req_data is None:
            return resp_invalid_data('Users', {}, msg=MSG_NO_DATA)

        confirm_password = req_data.pop('confirm_password')

        if not check_password_in_singup(req_data.get('password'), confirm_password):
            errors = {'password': MSG_PASSWORD_DIDNT_MATCH}
            return resp_invalid_data('Users', errors)

        try:
            query = get_user_by_id(user_id)
            user = schema.dump(query)
            data = update_schema.load(req_data)

        except IntegrityError:
            return resp_invalid_data('Users', IntegrityError.orig)

        email = data.get('email', None)

        if email and exists_email_in_user(email, user):
            return resp_ok('Users', {'email': MSG_ALREADY_EXISTS.format('user')})
        try:
            query.update(request.json)
            current_app.db.session.commit()

        except IntegrityError as err:
            return resp_already_exists('Users', err.orig)
        except ValidationError as err:
            return resp_exception('Users', description=err.__str__())
        except Exception as err:
            return resp_exception('Users', description=err.__str__())
        result = re.search("'.*'", str(data.keys())).group()
        return resp_ok('Users', MSG_RESOURCE_UPDATED.format('Fields'), data=result)

    def delete(self, user_id):

        schema = UserSchema()
        try:
            query = User.query.filter(User.id == user_id).first_or_404()

        except Exception as err:
            return resp_exception('Users', description=err.__str__())

        user = schema.dump(query)

        current_app.db.session.delete(query)
        current_app.db.session.commit()

        return resp_ok('Users', MSG_RESOURCE_DELETED.format('User'), data=user)
