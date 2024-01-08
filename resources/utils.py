from db import db


def save_bitacora(model, data):
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
