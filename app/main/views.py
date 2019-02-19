from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm , PitchFormL, CommentForm
from ..models import User, Pitch, Review,Comment
from flask_login import login_required, current_user

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''



    title = 'blooger.com'

    return render_template("index.html", title=title)
