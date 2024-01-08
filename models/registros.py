import datetime

from db import db


class Registro(db.Model):
    __tablename__ = "bit_registros"

    id = db.Column(db.Integer, primary_key=True)
    parametros = db.Column(db.JSON, nullable=True)
    respuesta = db.Column(db.JSON, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.UTC))
