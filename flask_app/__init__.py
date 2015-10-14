from flask import Flask, Blueprint
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import config.py

app = Flask(__name__)
app.config.from_pyfile(config.py)
db = SQLAlchemy(app)
ma = Marshmallow(app)

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)


# routes go here
from flask.ext.app.main.resources.artist import ArtistIDAPI

api.add_resource(ArtistIDAPI, '/artist/{id}')