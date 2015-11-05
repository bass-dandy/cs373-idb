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
api.add_resource(ArtistIDAPI, '/artists/<int:id>')
api.add_resource(ArtistNameAPI, '/artists/<string:artistName>')
api.add_resource(ArtistAllAPI, '/artists/')

from flask.ext.app.main.resources.song import SongIDAPI, SongNameAPI
api.add_resource(SongIDAPI, '/songs/<int:id>')
api.add_resource(SongNameAPI,'/songs/<string:songName>')


from flask.ext.app.main.resources.award import AwardIDAPI
api.add_resource(AwardIDAPI, '/awards/<id>')

from flask.ext.app.main.resources.concert import ConcertIDAPI
api.add_resource(ConcertIDAPI, '/concerts/<id>')

from flask.ext.app.main.resources.label import LabelIDAPI
api.add_resource(LabelIDAPI, '/labels/<id>')

from flask.ext.app.main.resources.release import ReleaseIDAPI, ReleaseNameAPI
api.add_resource(ReleaseIDAPI, '/releases/<int:id>')
api.add_resource(ReleaseNameAPI, '/releases/<string:releaseName>')

from flask.ext.app.main.resources.video import VideoIDAPI
api.add_resource(VideoIDAPI, '/videos/<id>')
