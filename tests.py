from models import *

from flask import Flash, json, jsonify
from unittest import TestCase, main
from models import Artist, Label, Concert, Release, Award, Song
from flask_app import app, db
from flask.ext.sqlalchemy import SQLAlchemy

class MusicMeccaModelsTests(TestCase):

    def setUp(self):
        db.configure_mappers()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    #--------------
    # Artist Tests
    #--------------

    def test_artist_by_id(self):
        db.session.add(Artist(name="Taylor Swift"))
        db.session.commit()

        artist = Artist.query.get(00001)
        assertEquals(artist.name == "Taylor Swift")

    def test_artist_by_name(self):
        db.session.add(Artist(name="Kendrick Lamar"))
        db.session.commit()

        artist = Artist.query.filter_by(name="Kendrick Lamar").first()
        assertEquals(artist.name == "Kendrick Lamar")

    def test_artist_not_available(self):
        artist = Artist.query().filter_by(name="Katy Perry").first()
        assertIsNone(artist)

    #---------------
    # Song Tests
    #---------------

    def test_song_by_id(self):
        db.session.add(Artist(name="Taylor Swift"))
        db.session.add(Song(name="Bad Blood",lyrics="Lyrics go here", artist=[00001, 00002]))
        db.session.commit()

        song = Song.query.get(00001)
        assertEquals(song.name, "Bad Blood")
        assertEquals(song.lyrics, "Lyrics go here")
        artist = Artist.query.get(song.artist[0])
        assertEquals(artist.name, "Taylor Swift")

    def test_song_by_name(self):
        db.session.add(Artist(name="Kendrick Lamar"))
        db.session.add(Song(name="m.A.A.d City", lyrics="Lyrics", artist=[00002]))
        db.session.commit()

        song = Song.query.filter_by(name="m.A.A.D City").first()
        assertEquals(song.name, "m.A.A.D City")
        assertEquals(song.lyrics, "Lyrics")
        artist = Artist.query.get(song.artist[0])
        assertEquals(artist.name, "Kendrick Lamar")
        



if __name__ == '__main__':
    main()