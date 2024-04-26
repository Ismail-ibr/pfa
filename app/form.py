from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,PasswordField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    name=StringField('Fullname',validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired()])    
    phonenumber=IntegerField('phone number',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('Submit')