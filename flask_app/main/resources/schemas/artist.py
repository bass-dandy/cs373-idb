from marshmallow import fields
from marshmallow import Schema
from .video import VideoSchema
from .label import LabelSchema
from .award import AwardSchema
from .concert import ConcertSchema
from .tvpresence import TVPresenceSchema
from .release import ReleaseSchema
from .song import SongSchema

class ArtistSchema(Schema):
    """Marshmallow Schema class for the Artist model."""
    id = fields.Integer()
    name = fields.String(required=True)
    bio = fields.String(allow_none=True)
    photo = fields.Raw()

    videos = fields.List(fields.Nested(VideoSchema))
    label = fields.List(fields.Nested(LabelSchema))
    awards = fields.List(fields.Nested(AwardSchema))
    concerts = fields.List(fields.Nested(ConcertSchema))
    tvpresence = fields.List(fields.Nested(TVPresenceSchema))
    releases = fields.List(fields.Nested(ReleaseSchema))
    songs = fields.List(fields.Nested(SongSchema))

