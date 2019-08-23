from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired


class Select_Movie(FlaskForm):
    movies = SelectField('movies', validators=[DataRequired()], coerce=int)
