from marshmallow import fields
from marshmallow import Schema


class AwardSchema(Schema):
    """Marshmallow Schema class for the Award model."""
    id = fields.Integer()
    name = fields.String(required=True)
    year = fields.String(allow_none=True)

    artist = fields.List(fields.Nested('ArtistSchema'))
