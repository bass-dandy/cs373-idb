from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from sqlalchemy import asc
from flask_app.main.models import Artist
from flask_app import app
from flask_app.main.resources.schemas.artist import ArtistSchema


class ArtistAllAPI(Resource):
    """All artists in Artist table"""

    def get(self):
        """get all artists"""
        try:
            #print("GET ALL THE ARTISTS")
            artists = Artist.query.order_by(asc(Artist.name)).all()
            #print(artists)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['ARTIST_NOT_FOUND'].format(id))

        return ArtistSchema().dump(artists, many=True).data

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
