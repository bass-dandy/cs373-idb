from marshmallow import fields
from marshmallow import Schema
from flask_app import ma


class LabelSchema(Schema):
    """Marshmallow Schema class for the Label model."""
    id = fields.Integer()
    name = fields.String(required=True)
    bio = fields.String(allow_none=True)
    small_image = fields.String()
    uri = ma.URLFor('.labelidapi', id='<id>')

    artists = fields.List(fields.Nested('ArtistSchema', only=['uri']))
