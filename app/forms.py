from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email

class Generadorqr(FlaskForm):
    email = StringField('Correo Electrónico', validators=[DataRequired("Por favor digite un correo"), Email()])
    submit = SubmitField('Generar QR')

    