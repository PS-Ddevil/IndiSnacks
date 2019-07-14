from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField

class SearchForm(FlaskForm):
    image_file = FileField('Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')