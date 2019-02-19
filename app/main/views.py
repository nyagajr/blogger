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
@main.route('/Interview',methods = ['GET', 'POST'])
@login_required
def Interview():

    pitch_form = PitchFormI()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        # cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch,user = current_user)
        new_pitch.save_pitch()

        #return redirect(url_for('index.html'))

    all_pitches = Pitch.get_category('Interview')

    title = 'Interview Pitch'

    return render_template("Interview.html", pitch_form = pitch_form, pitches = all_pitches)

