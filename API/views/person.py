from flask import Blueprint, current_app, request
from API.models.model import Person
from API.schemas.serealizer import PersonSchema


bp_person = Blueprint('person', __name__)


@bp_person.route('/api/insert', methods=['POST'])
def insert():
    ps = PersonSchema()
    person = ps.load(request.json)

    current_app.db.session.add(person)
    current_app.db.session.commit()
    return ps.jsonify(person), 201


@bp_person.route('/api/show', methods=['GET'])
def show():
    result = Person.query.all()
    return PersonSchema(many=True).jsonify(result), 200


@bp_person.route('/api/update', methods=['POST'])
def update():
    ...


@bp_person.route('/api/delete', methods=['GET'])
def delete():
    ...
