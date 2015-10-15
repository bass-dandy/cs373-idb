from marshmallow import fields
from marshmallow import Schema
from .artist import ArtistSchema
from .release import ReleaseSchema


class SongSchema(Schema):
    """Marshmallow Schema class for the Song model."""
    id = fields.Integer()
    name = fields.String(required=True)
    lyrics = fields.String(allow_none=True)

    artist = fields.List(fields.Nested(ArtistSchema))
    releases = fields.List(fields.Nested(ReleaseSchema))
