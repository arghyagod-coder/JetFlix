from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, URLField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError, URL
from jetflix.models import User 

class RegisterForm(FlaskForm):

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists! Try a different name!")


    def validate_email(self, email):
        user = User.query.filter_by(email_address=email.data).first()
        if user:
            raise ValidationError("Email Address already exists! Try a different email!")

    username = StringField(label='Enter your Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Enter Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    username = StringField(label='Enter your Username:', validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label="Sign In")