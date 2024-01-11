from typing import List

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request

from .schemas import RegistroSchema
from models import Registro

blp = Blueprint("registros", __name__, description="Operaciones para registros.")


@blp.route("/registros")
class Registros(MethodView):
    """Vista para registros."""

    @blp.response(200, RegistroSchema(many=True))
    def get(self) -> List[RegistroSchema]:
        """Función para obtener el listado de registros.

        :return: Listado de registros.
        """
        try:
            registros = Registro.query.all()
            return registros
        except KeyError:
            abort(404, message="Registros no encontradas.")
