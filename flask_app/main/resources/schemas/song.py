from marshmallow import fields
from marshmallow import Schema
from flask.ext.app import ma


class SongSchema(Schema):
    """Marshmallow Schema class for the Song model."""
    id = fields.Integer()
    name = fields.String(required=True)
    lyrics = fields.String(allow_none=True)
    uri = ma.URLFor('.songidapi', id='<id>')
    preview_url = fields.String(attribute='preview_url')
    disc_number = fields.Integer()
    track_num = fields.Integer()
    spotify_url = fields.String()
    duration = fields.Integer()

    releases = fields.List(fields.Nested('ReleaseSchema', only=['uri']))

    #video = fields.List(fields.Nested('VideoSchema'))
