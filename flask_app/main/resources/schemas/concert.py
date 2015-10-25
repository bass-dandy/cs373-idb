from marshmallow import fields
from marshmallow import Schema
from flask.ext.app import ma


class ConcertSchema(Schema):
    """Marshmallow Schema class for the Concert model."""
    id = fields.Integer()
    name = fields.String(required=True)
    location = fields.String(allow_none=True)
    date = fields.Date()
    uri = ma.URLFor('.concertidapi', id='<id>')


