from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class base_form(FlaskForm):
    api_key = StringField('API_KEY', validators=[DataRequired(), Length(min=2, max=35)])
    submit = SubmitField('Get Quotes')


class zenquotes_io(FlaskForm):
    api_key = StringField('API_KEY', validators=[DataRequired(), Length(min=2, max=35)])
    submit = SubmitField('Get Quotes')


class api_ninjas_com(FlaskForm):
    api_key = StringField('API_KEY', validators=[DataRequired(), Length(min=2, max=35)])
    submit = SubmitField('Get Quotes')


class quoteslate_vercel_app(FlaskForm):
    api_key = StringField('API_KEY', validators=[DataRequired(), Length(min=2, max=35)])
    submit = SubmitField('Get Quotes')



