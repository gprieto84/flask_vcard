from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'DC_Usuarios'

    correo = db.Column(db.String(120), primary_key=True)
    nombres = db.Column(db.String)
    apellidos =db.Column(db.String)
    extension = db.Column(db.Integer)
    celular = db.Column(db.String)
    empresa = db.Column(db.String(64))
    puesto = db.Column(db.String(128))
    pagina_web = db.Column(db.String(128))
    ciudad = db.Column(db.String(64))
    departamento = db.Column(db.String(64))
    area= db.Column(db.String(64))
