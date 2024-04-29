from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,PasswordField,EmailField
from wtforms.validators import DataRequired,Email,ValidationError
from app.models import Users

class SignUpForm(FlaskForm):
    name=StringField('Fullname',validators=[DataRequired()])
    email=EmailField('email',validators=[DataRequired(),Email()])    
    phonenumber=IntegerField('phone number',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('Sign Up')
    
    def validate_email(self,email):
        user=Users.query.filter_by(email=email.data).first()
        if user:
            raise  ValidationError("This email is already taken. Please choose a different one")

class LoginForm(FlaskForm):
    name=StringField('Full name',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('Log In')
    
