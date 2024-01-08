from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request

from .schemas import RegistroSchema
from db import registros

blp = Blueprint("registros", __name__, description="Operaciones para registros.")


@blp.route("/registros")
class Registros(MethodView):
    @blp.response(200, RegistroSchema(many=True))
    def get(self):
        try:
            return registros
        except KeyError:
            abort(404, message="Registros no encontradas.")