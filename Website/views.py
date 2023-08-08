#making blueprints with roots / urls inside for everything view related
from flask import Blueprint

views = Blueprint('views')

@views.route('/')
def home():
    pass