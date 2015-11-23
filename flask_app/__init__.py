from flask import Flask, Blueprint
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_envvar('CONFIG_PATH')

db = SQLAlchemy(app)
ma = Marshmallow(app)

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

# routes go here
from flask_app.main.resources.search import SearchAPI
api.add_resource(SearchAPI, '/')

from flask.ext.app.main.resources.artist import ArtistIDAPI, ArtistNameAPI, ArtistAllAPI
api.add_resource(ArtistIDAPI, '/artists/<int:id>')
api.add_resource(ArtistNameAPI, '/artists/<string:artistName>')
api.add_resource(ArtistAllAPI, '/artists', '/artists/')

from flask.ext.app.main.resources.song import SongIDAPI, SongNameAPI
api.add_resource(SongIDAPI, '/songs/<int:id>')
api.add_resource(SongNameAPI, '/songs/<string:songName>')


from flask.ext.app.main.resources.award import AwardIDAPI
api.add_resource(AwardIDAPI, '/awards/<id>')

from flask.ext.app.main.resources.concert import ConcertIDAPI
api.add_resource(ConcertIDAPI, '/concerts/<id>')

from flask.ext.app.main.resources.label import LabelIDAPI, LabelNameAPI, LabelAllAPI
api.add_resource(LabelIDAPI, '/labels/<int:id>')
api.add_resource(LabelNameAPI, '/labels/<string:labelName>')
api.add_resource(LabelAllAPI, '/labels', '/labels/')

from flask.ext.app.main.resources.release import ReleaseIDAPI, ReleaseNameAPI, ReleaseAllAPI
api.add_resource(ReleaseIDAPI, '/releases/<int:id>')
api.add_resource(ReleaseNameAPI, '/releases/<string:releaseName>')
api.add_resource(ReleaseAllAPI, '/releases', '/releases/')

from flask.ext.app.main.resources.discussion import ArtistDiscussionAPI, DiscussionAPI, DiscussionRepliesAPI
api.add_resource(ArtistDiscussionAPI, '/artists/<int:artist_id>/discussions')
api.add_resource(DiscussionRepliesAPI, '/artists/<int:artist_id>/discussions<int:discussion_id>')
api.add_resource(DiscussionAPI, '/discussions/<int:id>')

from flask.ext.app.main.resources.tests import TestAPI
api.add_resource(TestAPI, '/runtests/')

app.register_blueprint(api_bp)
