from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Release
from flask_app import app
from flask_app.main.resources.schemas.release import ReleaseSchema


class ReleaseIDAPI(Resource):
    """Single release through id"""

    def get(self, id):
        """Get release with id"""
        try:
            release = Release.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['RELEASE_NOT_FOUND'].format(id))

        return ReleaseSchema().dump(release).data
