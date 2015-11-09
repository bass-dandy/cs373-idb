from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Label
from flask_app import app
from flask_app.main.resources.schemas.artist import LabelSchema


class LabelAllAPI(Resource):
    """All labels in Label table"""

    def get(self):
        """get all labels"""
        try:
            labels = Label.query.all()
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['LABEL_NOT_FOUND'].format(id))

        return LabelSchema(many=True).dump(labels).data

class LabelIDAPI(Resource):
    """Single label through id"""

    def get(self, id):
        """Get label with id"""
        try:
            label = Label.query.get(id)
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['LABEL_NOT_FOUND'].format(id))

        return LabelSchema().dump(label).data

class LabelNameAPI(Resource):
    """List of labels with similar"""

    def get(self, labelName):
        """get label by name"""
        try:
            actualLabelName = labelName.replace("+", " ")
            #print(actualLabelName)
            labels = Label.query.filter_by(name=actualLabelName)
            #print(labels)
        except(DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['ARTIST_NOT_FOUND'].format(actualLabelName))

        return LabelSchema().dump(labels, many=True).data