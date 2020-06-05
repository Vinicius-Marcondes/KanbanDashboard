from flask import jsonify

# Third
from marshmallow import ValidationError

# Local
from .models import User


def check_password_in_singup(password: str, confirm_password: str):
    if not password:
        return False
    if not confirm_password:
        return False
    if not password == confirm_password:
        return False
    return True


def get_user_by_id(user_id: int):
    try:
        return User.objects.get(id == user_id)
    except ValidationError as err:
        return jsonify(err)


def exists_email_in_user(email: str, instance=None):
    user = None

    try:
        user = User.objects.get(email == email)
    except ValidationError as err:
        return jsonify(err)
    except User.objects.get(email, many=True):
        return True

    if instance and instance.id == user.id:
        return True


def get_user_by_email(email: str):
    try:
        return User.objects.get(email == email)
    except ValidationError as err:
        return jsonify(err)
