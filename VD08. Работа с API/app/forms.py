from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class form_with_key(FlaskForm):
    api_key = StringField('API_KEY', validators=[DataRequired(), Length(min=35, max=45)])
    submit = SubmitField('Получить цитату')

class form_without_key(FlaskForm):
    submit = SubmitField('Получить цитату')


