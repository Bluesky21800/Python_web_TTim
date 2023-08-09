#making blueprints with roots / urls inside for everything view related
from flask import Blueprint

views = Blueprint('views', __name__)

#decorator for route for main page
@views.route('/')
def home():
    return "<h1>test</h1>"