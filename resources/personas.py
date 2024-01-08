from typing import List

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request

from .schemas import PersonaBusquedaSchema, PersonaSchema, PersonaBusquedaRespSchema
from db import personas

blp = Blueprint("personas", __name__, description="Operaciones para personas.")


@blp.route("/personas")
class Personas(MethodView):
    @blp.response(200, PersonaSchema(many=True))
    def get(self):
        try:
            return personas
        except KeyError:
            abort(404, message="Personas no encontradas.")

    @blp.arguments(schema=PersonaBusquedaSchema)
    @blp.response(200, PersonaBusquedaRespSchema)
    def post(self, request_data):
        print(request_data)
        if "nombre" not in request_data:
            return {"encontrado": False}

        for persona in personas:
            if request_data["nombre"] == persona["nombre"]:
                return {"encontrado": True}

        return {"encontrado": False}
