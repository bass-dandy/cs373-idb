from marshmallow import fields, Schema
from .label import LabelSchema
from .release import ReleaseSchema
from .artist import ArtistSchema


class SearchSchema(Schema):
    """Marshmallow Schema class for the Artist model."""
    releases = fields.List(fields.Nested(ReleaseSchema, only=['name', 'small_image', 'uri']))
    artists = fields.List(fields.Nested(ArtistSchema, only=['name', 'small_image', 'uri']))
    labels = fields.List(fields.Nested(LabelSchema, only=['name', 'small_image', 'uri']))
