from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_envvar('CONFIG_PATH')

db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app)

# routes go here
from flask.ext.app.main.resources.hello_world import HelloWorldAPI
api.add_resource(HelloWorldAPI, '/')

from flask.ext.app.main.resources.artist import ArtistIDAPI, ArtistNameAPI, ArtistAllAPI
api.add_resource(ArtistIDAPI, '/api/artists/<int:id>')
api.add_resource(ArtistNameAPI, '/api/artists/<string:artistName>')
api.add_resource(ArtistAllAPI, '/api/artists/')

from flask.ext.app.main.resources.song import SongIDAPI, SongNameAPI
api.add_resource(SongIDAPI, '/api/songs/<int:id>')
api.add_resource(SongNameAPI,'/api/songs/<string:songName>')


from flask.ext.app.main.resources.award import AwardIDAPI
api.add_resource(AwardIDAPI, '/api/awards/<id>')

from flask.ext.app.main.resources.concert import ConcertIDAPI
api.add_resource(ConcertIDAPI, '/api/concerts/<id>')

from flask.ext.app.main.resources.label import LabelIDAPI, LabelNameAPI, LabelAllAPI
api.add_resource(LabelIDAPI, '/api/labels/<int:id>')
api.add_resource(LabelNameAPI, '/api/labels/<string:labelName>')
api.add_resource(LabelAllAPI, '/api/labels/')

from flask.ext.app.main.resources.release import ReleaseIDAPI, ReleaseNameAPI, ReleaseAllAPI
api.add_resource(ReleaseIDAPI, '/api/releases/<int:id>')
api.add_resource(ReleaseNameAPI, '/api/releases/<string:releaseName>')
api.add_resource(ReleaseAllAPI, '/api/releases/')

from flask.ext.app.main.resources.tests import TestAPI
api.add_resource(TestAPI, '/api/runtests/')

