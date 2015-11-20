from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from sqlalchemy import asc
from flask_app.main.models import Release
from flask_app import app
from flask_app.main.resources.schemas.release import ReleaseSchema

class ReleaseAllAPI(Resource):
    """All releases in Release table"""

    def get(self):
        """get all releases"""
        try:
            releases = Release.query.order_by(asc(Release.name)).all()
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['RELEASE_NOT_FOUND'].format(id))

        return ReleaseSchema().dump(releases, many=True).data

class ReleaseIDAPI(Resource):
    """Single release through id"""

    def get(self, id):
        """Get release with id"""
        try:
            release = Release.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['RELEASE_NOT_FOUND'].format(id))

        return ReleaseSchema().dump(release).data

class ReleaseNameAPI(Resource):
    """list of releases using a name"""

    def get(self, releaseName):
        """Get releases with name"""
        try:
            actualReleaseName = releaseName.replace('+', ' ')
            releases = Release.query.filter_by(name=actualReleaseName).order_by(asc(Release.name))
        except(DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['RELEASE_NOT_FOUND'].format(actualReleaseName))

        return ReleaseSchema().dump(releases, many=True).data
