from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm , PitchFormL, CommentForm
from ..models import User, Pitch, Review,Comment
from flask_login import login_required, current_user
