from flask.ext.restful import reqparse
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from sqlalchemy import asc, desc, func
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

class LabelNameAPI(Resource):
    """List of labels with similar"""

    def get(self, labelName):
        """get label by name"""
        try:
            actualLabelName = labelName.replace("+", " ")
            #print(actualLabelName)
            labels = Label.query.filter_by(name=actualLabelName).order_by(asc(Label.name))
            #print(labels)
        except(DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['ARTIST_NOT_FOUND'].format(actualLabelName))

        return LabelSchema().dump(labels, many=True).data


class LabelAllAPI(Resource):
    """All label in Label table"""

    def get(self):
        """get all label"""
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
                    label = Label.query.order_by(sort(func.lower(Label.name))).paginate(args['page'], args['pagesize']).items
                except Exception:
                    return {}
            else:
                label = Label.query.order_by(sort(func.lower(Label.name))).all()
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['RELEASE_NOT_FOUND'].format(id))

        return LabelSchema().dump(label, many=True).data