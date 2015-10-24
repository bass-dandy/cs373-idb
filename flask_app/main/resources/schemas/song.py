from marshmallow import fields
from marshmallow import Schema
from flask.ext.app import ma


class SongSchema(Schema):
    """Marshmallow Schema class for the Song model."""
    id = fields.Integer()
    name = fields.String(required=True)
    lyrics = fields.String(allow_none=True)
    uri = ma.URLFor('.songidapi', id='<id>')
    audio_url = fields.String()

    videos = fields.List(fields.Nested('VideoSchema'))
