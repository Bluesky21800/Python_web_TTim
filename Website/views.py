#making blueprints with roots / urls inside for everything view related
from flask import Blueprint

views = Blueprint('views')

#decorator for route for main page
@views.route('/')
def home():
    pass "<h1>test</h1>"