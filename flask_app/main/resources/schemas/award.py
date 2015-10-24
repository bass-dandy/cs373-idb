from marshmallow import fields
from marshmallow import Schema
from flask.ext.app import ma


class AwardSchema(Schema):
    """Marshmallow Schema class for the Award model."""
    id = fields.Integer()
    name = fields.String(required=True)
    year = fields.String(allow_none=True)
    uri = ma.URLFor('.awardidapi', id='<id>')

