from flask import request, jsonify
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from flask_app.main.models import Discussion, Artist, Reply
from flask_app import app, db
from flask_app.main.resources.schemas.discussion import DiscussionSchema, ReplySchema


# GET all / POST /artists/id/discussions
class ArtistDiscussionAPI(Resource):
    """All discussions through artist_id"""

    def get(self, artist_id):
        """Get discussion from artists with artist_id"""
        try:
            discussion = Artist.query.get(artist_id).discussion
            if discussion:
                return DiscussionSchema(many=True).dump(discussion).data
            else:
                abort(app.config['NOT_FOUND'], message=app.config['DISCUSSION_NOT_FOUND'].format(id))
        except (DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['DISCUSSION_NOT_FOUND'].format(id))



    def post(self, artist_id):
        """Post a discussion to an artist"""
        request.json['artistsId'] = int(artist_id)
        discussion, errors = DiscussionSchema().load(request.json)

        if errors:
            abort(app.config['UNPROCESSABLE_ENTITY'], message=jsonify(errors))

        db.session.add(discussion)
        db.session.commit()

        discussion_dump, errors = DiscussionSchema().dump(discussion)

        if errors:
            abort(app.config['UNPROCESSABLE_ENTITY'], message=jsonify(errors))

        return discussion_dump


# GET all / POST to a specific discussion /discussions/id/discussions/id
class DiscussionRepliesAPI(Resource):
    """Reply of a discussion"""

    def get(self, discussion_id):
        """Get reply"""
        try:
            reply = Reply.query.filter_by(discussion_id=discussion_id).one()
            if reply:
                return ReplySchema().dump(reply).data
            else:
                abort(app.config['NOT_FOUND'], message=app.config['DISCUSSION_NOT_FOUND'].format(id))
        except(DataError, NoResultFound):
            abort(app.config['NOT_FOUND'], message=app.config['DISCUSSION_NOT_FOUND'].format(discussion_id))

    def post(self, discussion_id):
        """Post a reply to a discussion"""
        request.json['discussionId'] = int(discussion_id)
        reply, errors = ReplySchema().load(request.json)

        if errors:
            abort(app.config['UNPROCESSABLE_ENTITY'], message=jsonify(errors))

        db.session.add(reply)
        db.session.commit()

        discussion_dump, errors = ReplySchema().dump(reply)

        if errors:
            abort(app.config['UNPROCESSABLE_ENTITY'], message=jsonify(errors))

        return discussion_dump

