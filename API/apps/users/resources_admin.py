from flask import request
from marshmallow import ValidationError

from sqlalchemy.exc import NoReferencedColumnError
from flask_restful import Resource
from apps.users.utils import get_user_by_id
from apps.messages import MSG_RESOURCE_FETCHED_PAGINATED, MSG_RESOURCE_FETCHED
from apps.responses import resp_ok, resp_exception, resp_does_not_exist
from sqlalchemy.orm.exc import NoResultFound

from .models import User
from .schemas import UserSchema


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
        result = get_user_by_id(user_id)

        return resp_ok('User', MSG_RESOURCE_FETCHED.format('User'), data=result)





