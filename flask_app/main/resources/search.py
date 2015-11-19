from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Artist, Label, Release
from flask_app import app
from flask_app.main.resources.schemas.search import SearchSchema
from flask_app.main.resources.schemas.release import ReleaseSchema
from flask_app.main.resources.schemas.label import LabelSchema
from flask_app.main.resources.schemas.artist import ArtistSchema
from flask_restful import Resource, abort
from flask.ext.restful import reqparse
from sqlalchemy.sql import text


class SearchAPI(Resource):
    def __init__(self, *args, **kwargs):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('q',
            location='args',
            type=str,
            help='A query string.',
            action='append')

    def get(self):
        args = self.reqparser.parse_args()
        terms = args['q']
        terms = terms[0]

        artists = {}
        releases = {}
        labels = {}

        try:
            artists = ArtistSchema(many=True).dump(Artist.query.filter(text('name ~ :reg')).params(reg=terms).all()).data
        except:
            pass
        try:
            releases = ReleaseSchema(many=True).dump(Release.query.filter(text('name ~ :reg')).params(reg=terms).all()).data
        except:
            pass
        try:
            labels = LabelSchema(many=True).dump(Label.query.filter(text('name ~ :reg')).params(reg=terms).all()).data
        except:
            pass

        try:
            search = {
                'artists': artists,
                'releases': releases,
                'labels': labels

            }
        except(DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message="Nothing matched your search.")

        return SearchSchema().dump(search).data