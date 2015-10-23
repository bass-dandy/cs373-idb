from flask_app import db


class Artist(db.Model):
    """ Main table for artist info
    """
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    bio = db.Column(db.String)
    photo = db.Column(db.BLOB)

    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'))
    videos = db.relationship('Video')
    label_id = db.Column(db.Integer, db.ForeignKey('labels.id'))
    label = db.relationship('Label')

    tvpresence_id = db.Column(db.Integer, db.ForeignKey('tvpresences.id'))
    tvpresence = db.relationship('TVPresence')

    awards_id = db.Column(db.Integer, db.ForeignKey('awards.id'))
    awards = db.relationship('Award')
    concerts_id = db.Column(db.Integer, db.ForeignKey('concerts.id'))
    concerts = db.relationship('Concert')
    release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    releases = db.relationship('Release')


class Label(db.Model):
    """ Main table for Label info
    """
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    bio = db.Column(db.String)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist')


class Concert(db.Model):
    """ Main table for artist concert info
    """
    __tablename__ = 'concerts'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(128))
    name = db.Column(db.String(128))
    date = db.Column(db.Date)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist')


class TVPresence(db.Model):
    """ Main table for artist tv presence info
    """
    __tablename__ = 'tvpresence'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))
    genre = db.Column(db.String(128))
    bio = db.Column(db.String)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist')


class Release(db.Model):
    """ Main table for artist releases info
    """
    __tablename__ = 'releases'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist')


class Video(db.Model):
    """ Main table for artist video info
    """
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist')

    
class Award(db.Model):
    """ Main table for artist awards
    """
    __tablename__ = 'awards'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist')


class Song(db.Model):
    """ Main table for artist song info
    """
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    lyrics = db.Column(db.String)
    name = db.Column(db.String(128))
    audio_url = db.Column(db.String)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist')
    release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    release = db.relationship('Release')


