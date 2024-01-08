from db import db


class Persona(db.Model):
    __tablename__ = "tbl_personas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
