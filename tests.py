import json
from unittest import main, TestCase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask_app.main.models import *

class MyTests(TestCase):
    #def setUp(self):
        #engine = create_engine("postgresql://musicmecca:mecca@localhost/musicmecca", echo=False)
        #self.session = sessionmaker
        #self.session.configure(bind=engine)

    def test_artist_id(self):
        artist = Artist.query.get(1)
        self.assertEqual("Chon", artist.name)
        #print("Artist Test 1\nExpected: Chon\nActual: "+artist['name'])

    def test_artist_name(self):
        artist = Artist.query.filter_by(name="Chon").first()
        self.assertEqual("Chon", artist.name)

    def test_artist_not_in_db(self):
        artist = Artist.query.filter_by(name="Justin Bieber").first()
        self.assertIsNone(artist)

    def test_release_id(self):
        release = Release.query.get(1)
        self.assertEqual("Grow", release.name)

    def test_release_name(self):
        release = Release.query.filter_by(name="Happiness").first()
        self.assertEqual("Happiness", release.name)

    def test_release_not_in_db(self):
        release = Release.query.filter_by(name="YOYOOYOYOY").first()
        self.assertIsNone(release)

    def test_label_id(self):
        label = Label.query.get(1)
        self.assertEqual("Rise Records", label.name)

    def test_label_name(self):
        label = Label.query.filter_by(name="Rise Records").first()
        self.assertEqual("Rise Records", label.name)

    def test_label_not_in_db(self):
        label = Label.query.filter_by(name="SLIMIIMIMIM").first()
        self.assertIsNone(label)

    def test_song_id(self):
        song = Song.query.get(1)
        self.assertEqual("Drift", song.name)

    def test_song_name(self):
        song = Song.query.filter_by(name="King Park").first()
        self.assertEqual("King Park", song.name)

    def test_song_not_in_db(self):
        song = Song.query.filter_by(name="BAD BLOOD").first()
        self.assertIsNone(song)

    def test_artist_from_release(self):
        release = Release.query.filter_by(name="Happiness").first()
        self.assertEqual("Dance Gavin Dance", release.artists[0].name)

if __name__ == "__main__":
    main()