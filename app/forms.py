from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms import TextField, TextAreaField

class UploadForm(FlaskForm):
    image   = FileField('Image', validators = 
    [FileRequired(), FileAllowed(['jpg', 'png', 'Only image files allowed'])])
    