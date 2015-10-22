from models import *

from flask import Flash, json, jsonify
from unittest import TestCase, main
from models import Artist, Label, Concert, Release, Award, Song, Video
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

        artist = Artist.query.get(1)
        self.assertEquals(artist.name == "Taylor Swift")

    def test_artist_by_name(self):
        db.session.add(Artist(name="Kendrick Lamar"))
        db.session.commit()

        artist = Artist.query.filter_by(name="Kendrick Lamar").first()
        self.assertEquals(artist.name == "Kendrick Lamar")

    def test_artist_not_available(self):
        artist = Artist.query().filter_by(name="Katy Perry").first()
        self.assertIsNone(artist)

    #---------------
    # Song Tests
    #---------------

    def test_song_by_id(self):
        db.session.add(Artist(name="Taylor Swift"))
        db.session.add(Song(name="Bad Blood",lyrics="Lyrics go here", artist=[00001, 00002]))
        db.session.commit()

        song = Song.query.get(1)
        self.assertEquals(song.name, "Bad Blood")
        self.assertEquals(song.lyrics, "Lyrics go here")
        artist = Artist.query.get(song.artist[0])
        self.assertEquals(artist.name, "Taylor Swift")

    def test_song_by_name(self):
        db.session.add(Artist(name="Kendrick Lamar"))
        db.session.add(Song(name="m.A.A.d City", lyrics="Lyrics", artist=[2]))
        db.session.commit()

        song = Song.query.filter_by(name="m.A.A.D City").first()
        self.assertEquals(song.name, "m.A.A.D City")
        self.assertEquals(song.lyrics, "Lyrics")
        artist = Artist.query.get(song.artist[0])
        self.assertEquals(artist.name, "Kendrick Lamar")

    def test_song_not_available(self):
        song = Song.query().filter_by(name="Roar").first()
        self.assertIsNone(song)

    #-------------
    # Video Tests
    #-------------

    def test_video_by_id(self):
        db.session.add(Video(name="Juicy", year="1994"))
        db.session.commit()

        video = Video.query.get(1)
        self.assertEquals(video.name, "Juicy")
        self.assertEquals(video.year, "1994")

    def test_video_by_name(self):
        db.session.add(Video(name="Roar", year="2013"))
        db.session.commit()

        video = Video.query.filter_by(name="Roar").first()

        self.assertEqual(video.name, "Roar")
        self.assertEqual(video.year, "2013")

    def test_video_not_available(self):
        video = Video.query.filter_by(name="Hiphopopotamus").first()

        self.assertIsNone(video)

    #--------------
    # Label Tests
    #--------------

    def test_label_by_id(self):
        db.session.add(Label(name="Def Jam Records", bio="Crazy stuff"))
        db.session.commit()

        label = Label.query.get(1)

        self.assertEqual(label.name, "Def Jam Records")
        self.assertEqual(label.bio, "Crazy stuff")

    def test_label_by_name(self):
        db.session.add(Label(name="A Cappella Records", bio="They love a capella"))
        db.session.commit()

        label = Label.query.filter_by(name="A Cappella Records").first()

        self.assertEqual(label.name, "A Cappella Records")
        self.assertEqual(label.bio, "They love a capella")

    def test_label_not_available(self):
        label = Label.query.filter_by(name="Barclay Records").first()
        self.assertIsNone(label)

    



if __name__ == '__main__':
    main()