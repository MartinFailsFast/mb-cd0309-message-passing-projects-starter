from flask import Flask, request, jsonify
from app.service import PersonService

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, welcome to the Flask app!"

# Create a new person
@app.route("/persons", methods=["POST"])
def create_person():
    payload = request.get_json()
    new_person = PersonService.create(payload)
    return jsonify(new_person.to_dict()), 201

# Retrieve a person by ID
@app.route("/persons/<int:person_id>", methods=["GET"])
def get_person(person_id):
    person = PersonService.retrieve(person_id)
    if not person:
        return jsonify({"message": "Person not found"}), 404
    return jsonify(person.to_dict())

# List all people
@app.route("/persons", methods=["GET"])
def list_people():
    people = PersonService.retrieve_all()
    return jsonify([person.to_dict() for person in people])

@app.route("/test", methods=["GET"])
def test_route():
    return jsonify("I Love You All")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
