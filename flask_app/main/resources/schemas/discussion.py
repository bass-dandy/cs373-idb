from marshmallow import fields, Schema, post_load
from flask_app.main.models import Discussion, Reply


def copy_dict_values_to_object_attrs(keys, source, dest):
    for key in keys:
        if key in source.keys():
            setattr(dest, key, source[key])


class ReplySchema(Schema):
    id = fields.Integer()
    reply = fields.String()
    discussionId = fields.Integer(attribute='discussion_id')

    @post_load
    def use_reply_object(self, item):
        if item is None:
            return item

        if 'id' in item.keys():
            reply = Reply.query.get(item['id'])
        else:
            reply = Reply()

        copy_keys = ['reply', 'discussion_id']

        copy_dict_values_to_object_attrs(copy_keys, item, reply)

        return reply


class DiscussionSchema(Schema):
    """Marshmallow Schema class for the Artist model."""
    id = fields.Integer()
    discussion = fields.String()
    artistsId = fields.Integer(attribute='artists_id')

    reply = fields.Nested('ReplySchema', allow_none=True)

    @post_load
    def use_discussion_object(self, item):
        if item is None:
            return item

        if 'id' in item.keys():
            discussion = Discussion.query.get(item['id'])
        else:
            discussion = Discussion()

        copy_keys = ['discussion', 'artists_id', 'reply']

        copy_dict_values_to_object_attrs(copy_keys, item, discussion)

        return discussion

