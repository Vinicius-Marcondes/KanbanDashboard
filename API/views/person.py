from flask import Blueprint, current_app, request, jsonify
from marshmallow import ValidationError

from apps.users.models import User, Roles
from apps.users.schemas import UserSchema


bp_user = Blueprint('user', __name__)


@bp_user.route('/api/insert', methods=['POST'])
def insert():
    user = UserSchema()
    try:
        result = user.load(request.json)
    except ValidationError as err:
        return err.messages, 406
    current_app.db.session.add(result)
    current_app.db.session.commit()
    return user.jsonify(result), 201


@bp_user.route('/api/show', methods=['GET'])
def show():
    try:
        result = User.query.join(Roles).filter(User.id == 2, Roles.role_id == 1)
    except ValidationError as err:
        return jsonify(err.messages), 404
    return UserSchema(many=True).jsonify(result), 200


@bp_user.route('/api/update/<key>', methods=['POST'])
def update(key: int):
    ps = UserSchema()
    query = User.query.filter(User.id == key)
    query.update(request.json)
    current_app.db.session.commit()
    return ps.jsonify(query.first())


@bp_user.route('/api/delete/<key>', methods=['GET'])
def delete(key: int):
    try:
        response = User.query.filter(User.id == key)
        if response is not None:
            return {'Message': 'No user found'}
    except ValidationError as err:
        return jsonify(err.messages)
    # User.query.filter(User.id == key).delete()
    current_app.db.session.commit()
    return UserSchema(many=True).jsonify(response)


