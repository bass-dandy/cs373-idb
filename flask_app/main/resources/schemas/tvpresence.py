from marshmallow import fields
from marshmallow import Schema
from .artist import ArtistSchema


class TVPresenceSchema(Schema):
    """Marshmallow Schema class for the TVPresence model."""
    id = fields.Integer()
    name = fields.String(required=True)
    year = fields.String(allow_none=True)
    genre = fields.String()
    info = fields.String()

    artist = fields.List(fields.Nested(ArtistSchema))

