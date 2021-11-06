# the front end side

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():  # this function will run whenever we go to the home 
    return render_template("home.html")
