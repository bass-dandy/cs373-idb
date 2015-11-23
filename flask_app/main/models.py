from flask_app import db


class Artist(db.Model):
    """
    Model of Artists
    A Artist is a single person or collection of people that attempt to create music
    """
    __tablename__ = 'artists'
    id = db.Column(db.Integer, db.Sequence('artist_id_seq'), primary_key=True)
    name = db.Column(db.String(128))
    bio = db.Column(db.String)
    large_image = db.Column(db.String)
    medium_image = db.Column(db.String)
    small_image = db.Column(db.String)
    spotify_url = db.Column(db.String)
    uri = db.Column(db.String)

    primary_label_id = db.Column(db.Integer, db.ForeignKey('labels.id', use_alter=True, name='fk_primary_label_id'))
    primary_label = db.relationship('Label', backref='artists', foreign_keys='Artist.primary_label_id')

    concerts = db.relationship('Concert', backref='artists', secondary='artist_concerts')
    releases = db.relationship('Release', backref='artists', secondary='artist_releases')
    awards = db.relationship('Award', backref='artists', secondary='artist_awards')

    discussion = db.relationship('Discussion')


class Discussion(db.Model):
    """
    Model for discussions
    """
    __tablename__ = 'discussions'
    id = db.Column(db.Integer, primary_key=True)
    discussion = db.Column(db.String)

    artists_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    reply = db.relationship('Reply', backref='Discussion')


class Reply(db.Model):
    """
    Model to support replies
    """
    __tablename__ = 'replies'
    id = db.Column(db.Integer, primary_key=True)
    reply = db.Column(db.String)
    discussion_id = db.Column(db.Integer, db.ForeignKey('discussions.id'))



class Label(db.Model):
    """
    Model for Label
    A label is a company that funds an artist to make music
    """
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    bio = db.Column(db.String)
    uri = db.Column(db.String)
    small_image = db.Column(db.String)


class ArtistConcert(db.Model):
    """
    Linking table for Artists and their Concerts
    """
    __tablename__ = 'artist_concerts'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    concert_id = db.Column(db.Integer, db.ForeignKey('concerts.id'))


class Concert(db.Model):
    """
    Model for Concert
    A Concert is an event where artists perform songs at certain location on a date. Usually apart of a tour
    """
    __tablename__ = 'concerts'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(128))
    name = db.Column(db.String(128))
    date = db.Column(db.Date)
    uri = db.Column(db.String)


class ArtistRelease(db.Model):
    """
    Linking table for Artists and their Releases
    """
    __tablename__ = 'artist_releases'
    id = db.Column(db.Integer, db.Sequence('artist_release_id_seq'), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))


class Release(db.Model):
    """
    Model for Release
    A release is generally an album of songs put out by an artist or multiple artists
    """
    __tablename__ = 'releases'
    id = db.Column(db.Integer, db.Sequence('release_id_seq'), primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))
    uri = db.Column(db.String)
    large_image = db.Column(db.String)
    medium_image = db.Column(db.String)
    small_image = db.Column(db.String)
    spotify_url = db.Column(db.String)
    type = db.Column(db.String)

    songs = db.relationship('Song', backref='releases', secondary='release_songs')


class ReleaseSong(db.Model):
    """
    Linking table for Releases and their songs
    """
    __tablename__ = 'release_songs'
    id = db.Column(db.Integer, primary_key=True)
    release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))


class ArtistAward(db.Model):
    """
    Linking table for Artists and their Awards
    """
    __tablename__ = 'artist_awards'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    award_id = db.Column(db.Integer, db.ForeignKey('awards.id'))


class Award(db.Model):
    """
    Model for Award
    An Award is reconginition of an artist doing something good.
    """
    __tablename__ = 'awards'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))
    uri = db.Column(db.String)


class Song(db.Model):
    """
    Model for Song
    A Song is a piece of work put out by an artist that can be listened to.
    """
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    lyrics = db.Column(db.String)
    name = db.Column(db.String(150))
    uri = db.Column(db.String)
    preview_url = db.Column(db.String)
    disc_number = db.Column(db.Integer)
    spotify_url = db.Column(db.String)
    track_num = db.Column(db.Integer)
    duration = db.Column(db.Integer)

