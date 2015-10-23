from marshmallow import fields
from marshmallow import Schema


class ConcertSchema(Schema):
    """Marshmallow Schema class for the Concert model."""
    id = fields.Integer()
    name = fields.String(required=True)
    location = fields.String(allow_none=True)
    date = fields.Date()

    artist = fields.List(fields.Nested('ArtistSchema'))

