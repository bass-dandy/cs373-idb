from marshmallow import fields
from marshmallow import Schema
from flask.ext.app import ma


class ReleaseSchema(Schema):
    """Marshmallow Schema class for the Release model."""
    id = fields.Integer()
    name = fields.String(required=True)
    year = fields.String(allow_none=True)
    uri = ma.URLFor('.releaseidapi', id='<id>')

    songs = fields.List(fields.Nested('Song'))

