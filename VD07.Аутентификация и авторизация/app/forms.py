from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=35)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Такая почта уже используется')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Запомни меня')
    submit = SubmitField('Login')


class EditProfile(FlaskForm):
    new_username = StringField('Username', validators=[DataRequired(), Length(min=2, max=35)])
    new_email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Save')

    def validate_username(self, new_username):
        user = User.query.filter_by(username=new_username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует')

    def validate_email(self, new_email):
        email = User.query.filter_by(email=new_email.data).first()
        if email:
            raise ValidationError('Такая почта уже используется')

