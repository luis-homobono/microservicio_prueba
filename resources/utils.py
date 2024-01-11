from typing import Dict
from db import db


def save_bitacora(model: object, data: Dict) -> bool:
    """Función para guardar el registro de búsqueda en la bitacora.

    :param model: Modelo de bitacora
    :param data: Datos a almacenar en la bitacora
    :return: Valor de validación de almacenamiento
    """
    try:
        # breakpoint()
        bitacora = model(**data)
        db.session.add(bitacora)
        db.session.commit()
        print("Saved")
        return True
    except:
        print("Not Saved")
        return False
