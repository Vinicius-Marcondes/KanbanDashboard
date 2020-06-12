from apps.responses import resp_exception
from flask import jsonify

# Third
from marshmallow import ValidationError

# Local
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
            raise Exception

    except ValidationError as err:
        return err.__dict__

    except Exception as err:
        return resp_exception('Users', description=err.__str__())

    return user


def exists_email_in_user(email: str):
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
        return User.query.filter(User.email == email).first_or_404()
    except ValidationError as err:
        return jsonify(err)
