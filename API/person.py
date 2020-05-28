from flask import Blueprint, current_app, request
from .model import Person
from .serealizer import PersonSchema


bp_person = Blueprint('person', __name__)


@bp_person.route('/insert', methods=['POST'])
def insert():
    ps = PersonSchema
    print(request.json)
    return {}


@bp_person.route('/show', methods=['GET'])
def show():
    ps = PersonSchema(many=True)
    result = Person.query.all()
    return ps.jsonify(result), 200


@bp_person.route('/update', methods=['POST'])
def update():
    ...


@bp_person.route('/delete', methods=['GET'])
def delete():
    ...
