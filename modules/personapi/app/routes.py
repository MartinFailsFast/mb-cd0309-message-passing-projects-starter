from flask import Blueprint

# Create a Blueprint for the routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, welcome to the Flask app!"

@main.route('/about')
def about():
    return "This is the about page."

