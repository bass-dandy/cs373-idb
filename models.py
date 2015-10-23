#from flask_app import db

from sqlalchemy import Table, Column, Integer, ForeignKey, BLOB, String, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
Many-to-Many relationship between artists and videos
"""
artists_video_association_table = Table('artistsVideo', Base.metadata,
                                       Column('artist_id', Integer, ForeignKey('artists.id')),
                                       Column('video_id', Integer, ForeignKey('videos.id')))
"""
Many-to-Many relationship between artists and concerts
"""
artists_concerts_association_table = Table('artistsConcerts', Base.metadata,
                                             Column('artist_id', Integer, ForeignKey('artists.id')),
                                             Column('concert_id', Integer, ForeignKey('concerts.id')))
"""
Many-to-Many relationship between artists and releases
"""
artists_releases_association_table = Table('artistsReleases', Base.metadata,
                                             Column('artist_id', Integer, ForeignKey('artists.id')),
                                             Column('release_id', Integer, ForeignKey('releases.id')))
"""
Many-to-Many relationship between artists and songs
"""
artists_songs_association_table = Table('artistsSongs', Base.metadata,
                                           Column('artist_id', Integer, ForeignKey('artists.id')),
                                           Column('song_id', Integer, ForeignKey('songs.id')))
"""
Many-to-Many relationship between releases and songs
"""
releases_songs_association_table = Table('releasesSongs', Base.metadata,
                                            Column('release_id', Integer, ForeignKey('releases.id')),
                                            Column('song_id', Integer, ForeignKey('songs.id')))


class Artist(Base):
    """
    Model of Artists
    A Artist is a single person or collection of people that attempt to create music
    """
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    bio = Column(String)
    photo = Column(BLOB)

    label_id = Column(Integer, ForeignKey('labels.id'))

    videos = relationship("Video", secondary=artists_video_association_table, backref="artists")
    concerts = relationship("Concert", secondary=artists_concerts_association_table, backref="artists")
    releases = relationship("Song", secondary=artists_releases_association_table, backref="artists")
    songs = relationship("Song", secondary=artists_songs_association_table, backref="artists")
    awards = relationship("Award", backref="artists")



    #video_id = Column(Integer, ForeignKey('videos.id'))
    #videos = relationship('Video')
    #label_id = Column(Integer, ForeignKey('labels.id'))
    #label = relationship('Label')
    #tvpresence_id = Column(Integer, ForeignKey('tvpresences.id'))
    #tvpresence = relationship('TVPresence')
    #awards_id = Column(Integer, ForeignKey('awards.id'))
    #awards = relationship('Award')
    #concerts_id = Column(Integer, ForeignKey('concerts.id'))
    #concerts = relationship('Concert')
    #release_id = Column(Integer, ForeignKey('releases.id'))
    #releases = relationship('Release')


class Label(Base):
    """
    Model for Label
    A label is a company that funds an artist to make music
    """
    __tablename__ = 'labels'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    bio = Column(String)

    artists = relationship("Artist", backref="labels")

    #artist_id = Column(Integer, ForeignKey('artists.id'))
    #artist = relationship('Artist')


class Concert(Base):
    """
    Model for Concert
    A Concert is an event where artists perform songs at certain location on a date. Usually apart of a tour
    """
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    location = Column(String(128))
    name = Column(String(128))
    date = Column(Date)

    #artist_id = Column(Integer, ForeignKey('artists.id'))
    #artist = relationship('Artist')


#class TVPresence(Base):
#    """ Main table for artist tv presence info
#    """
#    __tablename__ = 'tvpresence'
#    id = Column(Integer, primary_key=True)
#    year = Column(String(128))
#    name = Column(String(128))
#    genre = Column(String(128))
#    bio = Column(String)

#    artist_id = Column(Integer, ForeignKey('artists.id'))
#    artist = relationship('Artist')


class Release(Base):
    """
    Model for Release
    A release is generally an album of songs put out by an artist or multiple artists
    """
    __tablename__ = 'releases'
    id = Column(Integer, primary_key=True)
    year = Column(String(128))
    name = Column(String(128))

    songs = relationship('Song', secondary=releases_songs_association_table, backref='releases')

    #artist_id = Column(Integer, ForeignKey('artists.id'))
    #artist = relationship('Artist')


class Video(Base):
    """
    Model for Video
    A video a video version of a song generally a music video by an artist(s)
    """
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    year = Column(String(128))
    name = Column(String(128))
    song_id = Column(Integer, ForeignKey("songs.id"))


    #artist_id = Column(Integer, ForeignKey('artists.id'))
    #artist = relationship('Artist')

    
class Award(Base):
    """
    Model for Award
    An Award is reconginition of an artist doing something good.
    """
    __tablename__ = 'awards'
    id = Column(Integer, primary_key=True)
    year = Column(String(128))
    name = Column(String(128))

    artist_id = Column(Integer, ForeignKey('artists.id'))
    #artist = relationship('Artist')


class Song(Base):
    """
    Model for Song
    A Song is a piece of work put out by an artist that can be listened to.
    """
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    lyrics = Column(String)
    name = Column(String(128))
    audio_url = Column(String)
    videos = relationship("Video", backref="songs")

    #artist_id = Column(Integer, ForeignKey('artists.id'))
    #artist = relationship('Artist')
    #release_id = Column(Integer, ForeignKey('releases.id'))
    #release = relationship('Release')


