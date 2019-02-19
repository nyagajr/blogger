from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('add Comment')


class PitchFormL(FlaskForm):
    pitch = TextAreaField('add blog', validators=[Required()])
    submit = SubmitField('Submit')

class PitchFormP(FlaskForm):
    pitch = TextAreaField('Pitch Comment', validators=[Required()])
    my_category = SelectField('Category', choices=[('Promotion','Promotion')])
    submit = SubmitField('Submit')
