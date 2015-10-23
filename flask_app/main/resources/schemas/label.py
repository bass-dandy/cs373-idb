from marshmallow import fields
from marshmallow import Schema


class LabelSchema(Schema):
    """Marshmallow Schema class for the Label model."""
    id = fields.Integer()
    name = fields.String(required=True)
    bio = fields.String(allow_none=True)
    photo = fields.Raw()

    artist = fields.List(fields.Nested('ArtistSchema'))
