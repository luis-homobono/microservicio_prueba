from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

personas = [
    {
        "id": 1,
        "nombre": "Luis Eloy Homobono Fuentes"
    },
    {
        "id": 2,
        "nombre": "Sunset Villegas"
    },
    {
        "id": 3,
        "nombre": "Pumkin Fuentes"
    }
]

registros = [
    {
        "id": 1,
        "parametros": "{nombre}: 'Luis'",
        "respuesta": "{encontrado: true}",
        "fecha_creacion": "07/01/2024"
    },
    {
        "id": 2,
        "parametros": "{nombre}: 'Eloy'",
        "respuesta": "{encontrado: false}",
        "fecha_creacion": "07/01/2024"
    }
]