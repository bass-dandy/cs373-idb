from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app)

app.config.from_envvar('CONFIG_PATH')

# routes go here
from flask.ext.app.main.resources.hello_world import HelloWorldAPI
api.add_resource(HelloWorldAPI, '/')

from flask.ext.app.main.resources.artist import ArtistIDAPI
api.add_resource(ArtistIDAPI, '/artist/<id>')

# from flask.ext.app.main.resources.song import SongIDAPI
# api.add_resource(SongIDAPI, '/song/<id>')