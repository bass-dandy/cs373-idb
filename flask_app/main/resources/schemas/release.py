from marshmallow import fields
from marshmallow import Schema
from flask.ext.app import ma
from .song import SongSchema


class ReleaseSchema(Schema):
    """Marshmallow Schema class for the Release model."""
    id = fields.Integer()
    name = fields.String(required=True)
    year = fields.String(allow_none=True)
    large_image = fields.String()
    medium_image = fields.String()
    small_image = fields.String()
    spotify_url = fields.String()
    type = fields.String()
    uri = ma.URLFor('.releaseidapi', id='<id>')
    artists = fields.List(fields.Nested('ArtistSchema', only=["uri"]))
    songs = fields.List(fields.Nested('SongSchema', only=["uri"]))

