from flask.ext.restful import reqparse
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from sqlalchemy import asc, desc, func
from flask_app.main.models import Artist
from flask_app import app
from flask_app.main.resources.schemas.artist import ArtistSchema


class ArtistIDAPI(Resource):
    """Single artist through id"""

    def get(self, id):
        """Get artist with id"""
        try:
            artist = Artist.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['ARTIST_NOT_FOUND'].format(id))

        return ArtistSchema().dump(artist).data


class ArtistNameAPI(Resource):
    """list of artists using a name"""

    def get(self, artistName):
        """Get artists with name"""
        try:
            #print(artistName)
            actualArtistName = artistName.replace('+', ' ')
            artists = Artist.query.filter_by(name=actualArtistName).order_by(asc(Artist.name))
        except(DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['ARTIST_NOT_FOUND'].format(actualArtistName))

        return ArtistSchema().dump(artists, many=True).data


class ArtistAllAPI(Resource):
    """All artists in Artist table"""

    def get(self):
        """get all artists"""
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('order', type=str)
        parser.add_argument('pagesize', type=int)
        args = parser.parse_args()

        try:
            sort = asc
            if 'order' in args and args['order'] is not None:
                sort = asc if args['order'] == 'asc' else desc
            if 'page' in args and 'pagesize' in args and args['page'] is not None and args['pagesize'] is not None:
                try:
                    artists = Artist.query.order_by(sort(func.lower(Artist.name))).paginate(args['page'], args['pagesize']).items
                except Exception:
                    return {}
            else:
                artists = Artist.query.order_by(sort(func.lower(Artist.name))).all()
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['ARTIST_NOT_FOUND'].format(id))

        return ArtistSchema().dump(artists, many=True).data
