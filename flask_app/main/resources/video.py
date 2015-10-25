from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Video
from flask_app import app
from flask_app.main.resources.schemas.video import VideoSchema


class VideoIDAPI(Resource):
    """Single Video through id"""

    def get(self, id):
        """Get Video with id"""
        try:
            video = Video.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['VIDEO_NOT_FOUND'].format(id))

        return VideoSchema().dump(video).data
