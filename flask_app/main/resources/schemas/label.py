from marshmallow import fields
from marshmallow import Schema
from flask.ext.app import ma


class LabelSchema(Schema):
    """Marshmallow Schema class for the Label model."""
    id = fields.Integer()
    name = fields.String(required=True)
    bio = fields.String(allow_none=True)
    photo = fields.Raw()
    uri = ma.URLFor('.labelidapi', id='<id>')

    artists = fields.Nested('Artist', only=['uri'])
