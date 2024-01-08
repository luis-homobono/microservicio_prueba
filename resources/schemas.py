from marshmallow import fields, Schema

class PersonaSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.Str(required=True)


class PersonaBusquedaSchema(Schema):
    nombre = fields.Str(required=False)


class PersonaBusquedaRespSchema(Schema):
    encontrado = fields.Bool(required=True)


class RegistroSchema(Schema):
    id = fields.Integer(dump_only=True)
    parametros = fields.Str(required=True)
    respuesta = fields.Str(required=True)
    fecha_creacion = fields.Str(required=True)
