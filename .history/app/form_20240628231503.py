from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,PasswordField,EmailField,DateField,FloatField
from wtforms.validators import DataRequired,Email,ValidationError,NumberRange
from app.models import Users,Transaction
import datetime

class SignUpForm(FlaskForm):
    name=StringField('Fullname',validators=[DataRequired()], render_kw={"class": "form-label form-control","placeholder":"Enter your username"})
    email=EmailField('email',validators=[DataRequired(),Email()], render_kw={"class": "form-label form-control","placeholder":"Enter your email"})    
    phonenumber=IntegerField('phone number',validators=[DataRequired()], render_kw={"class": "form-label form-control","placeholder":"Enter your phonenumber"})
    password=PasswordField('password',validators=[DataRequired()], render_kw={"class": "form-label form-control","placeholder":".................","aria-describedby":"password"})
    submit=SubmitField('Sign Up', render_kw={"class": "btn btn-primary d-grid w-100"})
    
    def validate_email(self,email):
        user=Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email is already taken. Please choose a different one")

class LoginForm(FlaskForm):
    name=StringField('Full name',validators=[DataRequired()], render_kw={"class": "form-label"})
    password=PasswordField('password',validators=[DataRequired()], render_kw={"class": "form-label"})
    submit=SubmitField('Log In', render_kw={"class": "btn btn-primary d-grid w-100"})
    
class AddTransactionForm(FlaskForm):
    amount=FloatField('Transaction amount',validators=[DataRequired()], render_kw={"class": "form-label"})
    category=StringField('Transaction category',validators=[DataRequired()], render_kw={"class": "form-label"})
    date=DateField('Transaction date',default=datetime.datetime.now(), render_kw={"class": "form-label"})
    submit=SubmitField('Add Transaction', render_kw={"class": "btn btn-primary d-grid w-100"})
    
    
class filterbymonth(FlaskForm):
    date=IntegerField('email-username',validators=[NumberRange(min=1,max=12)],render_kw={"class": "form-control","placeholder": "Enter month (1-12)", "id":"email"})
    submit=SubmitField('Filter',render_kw={"class": "btn btn-sm btn-outline-secondary mt-2"})
class ModifyTransaction(FlaskForm):
    id=IntegerField('Transaction id',validators=[DataRequired()])
    amount=FloatField('New Amount',validators=[DataRequired()], render_kw={"class": "form-label"})
    category=StringField('New category',validators=[DataRequired()], render_kw={"class": "form-label"})
    submit=SubmitField('Modify',render_kw={"class": "btn btn-primary d-grid w-100"})

class DeleteTransaction(FlaskForm):
    id=IntegerField('Transaction id',validators=[DataRequired()])
    submit=SubmitField('Delete',render_kw={"class": "btn btn-danger d-grid w-100"})