from apps.responses import resp_does_not_exist, resp_exception, resp_ok
from apps.messages import MSG_RESOURCE_FETCHED
from flask import jsonify, json

# Third
from marshmallow import ValidationError

# Local
from sqlalchemy.exc import NoReferencedColumnError
from sqlalchemy.orm.exc import MultipleResultsFound

from .models import User
from .schemas import UserSchema


def check_password_in_singup(password: str, confirm_password: str):
    if not password:
        return False
    if not confirm_password:
        return False
    if not password == confirm_password:
        return False
    return True


def get_user_by_id(user_id: int):
    """
    Return a user based on the filter(user.id == id_user)
    :param user_id: id of the user you want to find
    :return: obj
    """

    try:
        user = User.query.filter(User.id == user_id)
        result = UserSchema(many=True).dump(user)
        if not result:
            raise NoReferencedColumnError

    except ValidationError as err:
        return err.__dict__

    except Exception as err:
        return resp_exception('Users', description=err.__str__())

    return user


def exists_email_in_user(email: str, instance=None):
    user = None

    try:
        user = User.query.filter(User.email == email)
        result = UserSchema(many=True).dump(user)

        if not result:
            return False

    except ValidationError as err:
        return jsonify(err)
    except MultipleResultsFound:
        return True


def get_user_by_email(email: str):
    try:
        return User.objects.get(email == email)
    except ValidationError as err:
        return jsonify(err)
