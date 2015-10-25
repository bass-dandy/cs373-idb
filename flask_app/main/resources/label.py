from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Label
from flask_app import app
from flask_app.main.resources.schemas.artist import LabelSchema


class LabelIDAPI(Resource):
    """Single label through id"""

    def get(self, id):
        """Get label with id"""
        try:
            label = Label.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['LABEL_NOT_FOUND'].format(id))

        return LabelSchema().dump(label).data
