#making blueprints with roots / urls inside for everything view related
from flask import Blueprint, render_template


views = Blueprint('views', __name__)

#decorator for route for main page
@views.route('/')
def home():
    return render_template("home.html")
