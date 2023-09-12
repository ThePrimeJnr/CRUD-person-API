from flask import jsonify, request, abort
from . import app, db
from .models import Person

# CREATE A PERSON
@app.route('/api', methods=['POST'])
def create_person():
    try:
        person = Person(
            name=request.json.get('name')
        )
        db.session.add(person)
        db.session.commit()
        return jsonify(person.to_json()), 201
    except Exception as e:
        return {"Error": "Failed to Create Person"}, 400

# READ ALL PERSONS
@app.route("/api", methods=["GET"])
def get_persons():
    persons = Person.query.all()
    return jsonify([person.to_json() for person in persons])

# READ A PERSON BY ID
@app.route("/api/<int:user_id>", methods=["GET"])
def get_person(user_id):
    try:
        person = Person.query.get(user_id)
        return jsonify(person.to_json())
    except Exception as e:
        return {"Error": "Not Found"}, 404

# UPDATE A PERSON BY ID
@app.route('/api/<int:user_id>', methods=['PUT', 'PATCH'])
def update_person(user_id):
    try:
        person = Person.query.get(user_id)
        person.name = request.json.get('name', person.name)
        db.session.commit()
        return jsonify(person.to_json())
    except Exception as e:
        return {"Error": "Not Found"}, 404

# DELETE A PERSON
@app.route("/api/<int:user_id>", methods=["DELETE"])
def delete_person(user_id):
    try:
        person = Person.query.get(user_id)
        db.session.delete(person)
        db.session.commit()
        return jsonify({'result': True})
    except Exception as e:
        return {"Error": "Not Found"}, 404

