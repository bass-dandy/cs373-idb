from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
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
