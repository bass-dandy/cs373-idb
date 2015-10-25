from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Award
from flask_app import app
from flask_app.main.resources.schemas.award import AwardSchema


class AwardIDAPI(Resource):
    """Single award through id"""

    def get(self, id):
        """Get award with id"""
        try:
            award = Award.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['AWARD_NOT_FOUND'].format(id))

        return AwardSchema().dump(award).data
