from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 


from .config import config_by_name

db = SQLAlchemy()
ms = Marshmallow()

def createApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    ms.init_app(app)
    return app

