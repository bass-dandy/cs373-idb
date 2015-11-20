from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Concert
from flask_app import app
from flask_app.main.resources.schemas.concert import ConcertSchema


class ConcertIDAPI(Resource):
    """Single concert through id"""

    def get(self, id):
        """Get concert with id"""
        try:
            concert = Concert.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['CONCERT_NOT_FOUND'].format(id))

        return ConcertSchema().dump(concert).data
