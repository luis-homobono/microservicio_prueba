"""
Script para generar datos de prueba haciendo uso de librería faker
"""
from faker import Faker

from models.personas import Persona
from app import create_app
from db import db

fake = Faker()

with create_app().app_context() as app_context:
    for record in range(200):
        persona = Persona(nombre=fake.name())
        db.session.add(persona)
        db.session.commit()

print("Se lleno la base de datos")
