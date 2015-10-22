from flask_app import db

#from sqlalchemy import Table, Column, Integer, ForeignKey
#from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
Many-to-Many relationship between artists and videos
"""
artists_video_association_table = db.Table('artistsVideo', Base.metadata,
                                       db.Column('artist_id', db.Integer, db.ForeignKey('artists.id')),
                                       db.Column('video_id', db.Integer, db.ForeignKey('videos.id')))
"""
Many-to-Many relationship between artists and concerts
"""
artists_concerts_association_table = db.Table('artistsConcerts', Base.metaData,
                                             db.Column('artist_id', db.Integer, db.ForeignKey('artists.id')),
                                             db.Column('concert_id', db.Integer, db.ForeignKey('concerts.id')))
"""
Many-to-Many relationship between artists and releases
"""
artists_releases_association_table = db.Table('artistsReleases', Base.metaData,
                                             db.Column('artist_id', db.Integer, db.ForeignKey('artists.id')),
                                             db.Column('release_id', db.Integer, db.ForeignKey('releases.id')))
"""
Many-to-Many relationship between artists and songs
"""
artists_songs_association_table = db.Table('artistsSongs', Base.metaData,
                                           db.Column('artist_id', db.Integer, db.ForeignKey('artists.id')),
                                           db.Column('song_id', db.Integer, db.ForeignKey('songs.id')))
"""
Many-to-Many relationship between releases and songs
"""
releases_songs_association_table = db.Table('releasesSongs', Base.metaData,
                                            db.Column('release_id', db.Integer, db.ForeignKey('releases.id')),
                                            db.Column('song_id', db.Integer, db.ForeignKey('songs.id')))


class Artist(db.Model):
    """
    Model of Artists

    """
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    bio = db.Column(db.String)
    photo = db.Column(db.BLOB)

    label_id = db.Column(db.Integer, db.ForeignKey('labels.id'))

    videos = db.relationship("Video", secondary=artists_video_association_table, backref="artists")
    concerts = db.relationship("Concert", secondary=artists_concerts_association_table, backref="artists")
    releases = db.relationship("Song", secondary=artists_releases_association_table, backref="artists")
    songs = db.relationship("Song", secondary=artists_songs_association_table, backref="artists")
    awards = db.relationship("Award", backref="artists")



    #video_id = db.Column(db.Integer, db.ForeignKey('videos.id'))
    #videos = db.relationship('Video')
    #label_id = db.Column(db.Integer, db.ForeignKey('labels.id'))
    #label = db.relationship('Label')
    #tvpresence_id = db.Column(db.Integer, db.ForeignKey('tvpresences.id'))
    #tvpresence = db.relationship('TVPresence')
    #awards_id = db.Column(db.Integer, db.ForeignKey('awards.id'))
    #awards = db.relationship('Award')
    #concerts_id = db.Column(db.Integer, db.ForeignKey('concerts.id'))
    #concerts = db.relationship('Concert')
    #release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    #releases = db.relationship('Release')


class Label(db.Model):
    """
    Model for Label
    A label is a company that funds an artist to make music
    """
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    bio = db.Column(db.String)

    artists = db.relationship("Artist", backref="labels")

    #artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    #artist = db.relationship('Artist')


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

    #artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    #artist = db.relationship('Artist')


#class TVPresence(db.Model):
#    """ Main table for artist tv presence info
#    """
#    __tablename__ = 'tvpresence'
#    id = db.Column(db.Integer, primary_key=True)
#    year = db.Column(db.String(128))
#    name = db.Column(db.String(128))
#    genre = db.Column(db.String(128))
#    bio = db.Column(db.String)

#    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
#    artist = db.relationship('Artist')


class Release(db.Model):
    """
    Model for Release
    A release is generally an album of songs put out by an artist or multiple artists
    """
    __tablename__ = 'releases'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))

    songs = db.relationship('Song', secondary=releases_songs_association_table, backref='releases')

    #artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    #artist = db.relationship('Artist')


class Video(db.Model):
    """
    Model for Video
    A video a video version of a song generally a music video by an artist(s)
    """
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))


    #artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    #artist = db.relationship('Artist')

    
class Award(db.Model):
    """
    Model for Award
    An Award is reconginition of an artist doing something good.
    """
    __tablename__ = 'awards'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(128))
    name = db.Column(db.String(128))

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    #artist = db.relationship('Artist')


class Song(db.Model):
    """
    Model for Song
    A Song is a piece of work put out by an artist that can be listened to.
    """
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    lyrics = db.Column(db.String)
    name = db.Column(db.String(128))
    audio_url = db.Column(db.String)
    videos = db.relationship("Video", backref="songs")

    #artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    #artist = db.relationship('Artist')
    #release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    #release = db.relationship('Release')


