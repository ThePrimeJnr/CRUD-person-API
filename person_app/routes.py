from flask import jsonify, request, abort
from . import app, db
from .models import Person
import re

# CREATE A PERSON
@app.route('/api', methods=['POST'])
def create_person():
    try:
        name = request.json.get('name')
        if not name:
            return jsonify({'error': 'Name is required'}), 400

        if not re.match("^[A-Za-z0-9\s]*$", name):
            return jsonify({'error': 'Invalid characters in name'}), 400

        if len(name) > 50:
            return jsonify({'error': 'Name is too long'}), 400

        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        return jsonify({'message': f'{name} created successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create a person'}), 500

# READ ALL PERSONS
@app.route("/api", methods=["GET"])
def get_persons():
    persons = Person.query.all()
    return jsonify([person.to_json() for person in persons]), 200

# READ A PERSON BY ID
@app.route("/api/<int:user_id>", methods=["GET"])
def get_person(user_id):
    try:
        if user_id <= 0:
            return {"error": "Invalid user_id"}, 400

        if person := Person.query.get(user_id):
            return jsonify(person.to_json()), 200
        else:
            return {"error": "Person not found"}, 404
    except SQLAlchemyError as e:
        return {"error": "Database error"}, 500


# UPDATE A PERSON BY ID
@app.route('/api/<int:user_id>', methods=['PUT', 'PATCH'])
def update_person(user_id):
    try:
        if person := Person.query.get(user_id):
            name = request.json.get('name', person.name)
            person.name = name
            db.session.commit()
            return jsonify({'message': f'{name} updated successfully'}), 200
        else:
            return jsonify({'error': 'Person not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to update the person'}), 500

# DELETE A PERSON
@app.route("/api/<int:user_id>", methods=["DELETE"])
def delete_person(user_id):
    try:
        if person := Person.query.get(user_id):
            name = person.name
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': f'{name} deleted successfully'}), 200
        else:
            return jsonify({'error': 'Person not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to delete the person'}), 500

# INVALID ENDPOINT
@app.route("/api/<path:invalid>", methods=['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def handle_invalid_endpoint(invalid):
    return {"error": "Invalid URL parameter"}, 400
