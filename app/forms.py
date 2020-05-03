from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired(message='A description is required.')])
    uploadImage = FileField('Upload Photo', validators=[FileRequired('Please select a photo to upload.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Please upload image files only.')])
