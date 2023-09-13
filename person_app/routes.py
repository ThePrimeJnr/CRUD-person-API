from flask import jsonify, request, abort
from . import app, db
from .models import Person

# CREATE A PERSON
@app.route('/api', methods=['POST'])
def create_person():
    try:
        name = request.json.get('name')
        if name:
            person = Person(name=name)
            db.session.add(person)
            db.session.commit()
            return jsonify({'message': f'{name} created successfully'}), 201
        else:
            return jsonify({'error': 'Name is required'}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to create a person'}), 500

# UPDATE A PERSON BY ID
@app.route('/api/<int:user_id>', methods=['PUT', 'PATCH'])
def update_person(user_id):
    try:
        person = Person.query.get(user_id)
        if person:
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
        person = Person.query.get(user_id)
        if person:
            name = person.name
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': f'{name} deleted successfully'}), 200
        else:
            return jsonify({'error': 'Person not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to delete the person'}), 500

