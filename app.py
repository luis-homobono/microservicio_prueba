from flask import Flask
from flask_smorest import Api

from resources.personas import blp as PersonasBlueprint
from resources.registros import blp as RegistroBluepint
from config import Config
from db import db
import models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(PersonasBlueprint)
    api.register_blueprint(RegistroBluepint)

    return app
