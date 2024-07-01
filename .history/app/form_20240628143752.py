from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,PasswordField,EmailField,DateField,FloatField
from wtforms.validators import DataRequired,Email,ValidationError,NumberRange
from app.models import Users,Transaction
import datetime

class SignUpForm(FlaskForm):
    name=StringField('Fullname',validators=[DataRequired()])
    email=EmailField('email',validators=[DataRequired(),Email()])    
    phonenumber=IntegerField('phone number',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('Sign Up')
    
    def validate_email(self,email):
        user=Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email is already taken. Please choose a different one")

class LoginForm(FlaskForm):
    name=StringField('Full name',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('Log In')
    
class AddTransactionForm(FlaskForm):
    amount=FloatField('Transaction amount',validators=[DataRequired()])
    category=StringField('Transaction category',validators=[DataRequired()])
    date=DateField('Transaction date',default=datetime.datetime.now())
    submit=SubmitField('Add Transaction')
    
    
class filterbymonth(FlaskForm):
    date=IntegerField('month',validators=[NumberRange(min=1,max=12)],render_kw={"class": "form-control","placeholder": "Enter month (1-12)", "id":"email" ,"name":"email-username"})
    submit=SubmitField('Filter')
class ModifyTransaction(FlaskForm):
    id=IntegerField('Transaction id',validators=[DataRequired()])
    amount=FloatField('New Amount',validators=[DataRequired()])
    category=StringField('New category',validators=[DataRequired()])
    submit=SubmitField('Modify')