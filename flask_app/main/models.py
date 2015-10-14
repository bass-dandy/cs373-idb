from flask_app import db


class Artist(db.Model):
    """ Main table for artist info
    """
    __tablename__ = 'artists'


class Label(db.Model):
    """ Main table for Label info
    """
    __tablename__ = 'labels'


class Concert(db.Model):
    """ Main table for artist concert info
    """
    __tablename__ = 'shows'


class TVPresence(db.Model):
    """ Main table for artist tv presence info
    """
    __tablename__ = 'tvpresence'


class Release(db.Model):
    """ Main table for artist releases info
    """
    __tablename__ = 'releases'


class Video(db.Model):
    """ Main table for artist video info
    """
    __tablename__ = 'videos'
    
class Award(db.Model):
    """ Main table for artist awards
    """
    __tablename__ = 'awards


class Song(db.Model):
    """ Main table for artist song info
    """
    __tablename__ = 'songs'


class Feature(db.Model):
    """ Main table for artist feature info
    """
    __tablename__ = 'features'

