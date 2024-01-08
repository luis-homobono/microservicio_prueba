import pytest
import json

from app import create_app
from models import Persona


def test_obtener_personas():
    with create_app().test_client() as client:
        response = client.get("/personas")

        assert response.status_code == 200

def test_prueba_busqueda():
    with create_app().test_client() as client:
        response = client.post(
            "/personas", 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps({'nombre': 'Luis'}))

        data = json.loads(response.text)

        assert response.status_code == 200
        assert "encontrado" in data.keys()
        assert data["encontrado"] == True
