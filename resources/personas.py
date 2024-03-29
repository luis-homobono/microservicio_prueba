from typing import List, Dict

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import Response

from .schemas import PersonaBusquedaSchema, PersonaSchema, PersonaBusquedaRespSchema
from .utils import save_bitacora
from models import Persona, Registro

blp = Blueprint("personas", __name__, description="Operaciones para personas.")


@blp.route("/personas")
class Personas(MethodView):
    """Vista para recurso de personas"""

    @blp.response(200, PersonaSchema(many=True))
    def get(self) -> List[Persona]:
        """Metodo get para obtener listado de personas

        :return: Listado de personas
        """
        try:
            personas = Persona.query.all()
            return personas
        except KeyError:
            abort(404, message="Personas no encontradas.")

    @blp.arguments(schema=PersonaBusquedaSchema)
    @blp.response(200, PersonaBusquedaRespSchema)
    def post(self, request_data: PersonaBusquedaSchema) -> Dict:
        """Método POST para busqueda de personas a partir de los datos de una petición.

        :param request_data: parametros de la solicitud
        :return: Diccionario
        """
        encontrado = False
        if "nombre" in request_data:
            query = Persona.query.filter(
                Persona.nombre.ilike(f"%{request_data['nombre']}%")
            ).all()
            if len(query) > 0:
                encontrado = True

        respuesta = {"encontrado": encontrado}
        bitacora = {"parametros": request_data, "respuesta": respuesta}
        save_bitacora(model=Registro, data=bitacora)

        return respuesta
