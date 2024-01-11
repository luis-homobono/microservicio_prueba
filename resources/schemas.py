from marshmallow import fields, Schema


class PersonaSchema(Schema):
    """Schema para datos de persona."""
    id = fields.Integer(dump_only=True)
    nombre = fields.Str(required=True)


class PersonaBusquedaSchema(Schema):
    """Schema para buscar persona."""
    nombre = fields.Str(required=False)


class PersonaBusquedaRespSchema(Schema):
    """Schema de respuesta de busqueda de persona."""
    encontrado = fields.Bool(required=True)


class RegistroSchema(Schema):
    """Schema de registros."""
    id = fields.Integer(dump_only=True)
    parametros = fields.Str(required=True)
    respuesta = fields.Str(required=True)
    fecha_creacion = fields.Str(required=True)
