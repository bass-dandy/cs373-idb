from marshmallow import fields, Schema
from flask.ext.app import ma
from .label import LabelSchema
from .award import AwardSchema
from .concert import ConcertSchema
from .release import ReleaseSchema


class ArtistSchema(Schema):
    """Marshmallow Schema class for the Artist model."""
    id = fields.Integer()
    name = fields.String(required=True)
    bio = fields.String(allow_none=True)
    # photo = fields.Raw()
    uri = ma.URLFor('.artistidapi', id='<id>')

    primaryLabel = fields.Nested(LabelSchema, attribute='primary_label')

    awards = fields.List(fields.Nested(AwardSchema))
    concerts = fields.List(fields.Nested(ConcertSchema))
    releases = fields.List(fields.Nested(ReleaseSchema))

