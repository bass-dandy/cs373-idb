from flask import Flash, json, jsonify
from unittest import TestCase, main
from flask_app.main.models import Artist, Label, Concert, Release, Award, Song, Video
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


    #---------------
    # Concert Tests
    #---------------

    def test_concert_by_id(self):
        db.session.add(Concert(location="Austin", name="Taylor Swift 1989 Tour"))
        db.session.commit()

        concert = Concert.query.get(1)

        self.assertEqual(concert.location, "Austin")
        self.assertEqual(concert.name, "Taylor Swift 1989 Tour")

    def test_concert_by_location(self):
        db.session.add(Concert(location="Austin", name="Taylor Swift 1989 Tour"))
        db.session.commit()

        concerts = Concert.query.filter_by(location="Austin")
        self.assertEquals(concerts[0].name, "Taylor Swift 1989 Tour")

    def test_concert_not_available(self):
        concerts = Concert.query.filter_by(location="Anchorage").first()
        self.assertIsNone(concerts)

    #---------------
    # Release Tests
    #---------------

    def test_release_by_id(self):
        db,session.add(Release(name="1989", year="2015"))
        db.session.commit()

        release = Release.query.get(1)

        self.assertEqual(release.name, "1989")
        self.assertEqual(release.year, "2015")

    def test_release_by_name(self):
        db.session.add(Release(name="Revival", year="2015"))
        db.session.commit()

        release = Release.query.filter_by(name="Revival").first()

        self.assertEqual(release.name, "Revival")
        self.assertEqual(release.year, "2015")

    def test_release_not_available(self):
        release = Release.query.filter_by(name="Unbreakable").first()
        self.assertIsNone(release)


    #-------------
    # Award Tests
    #-------------

    def test_award_by_id(self):
        db.session.add(Award(name="Best Artist", year="2015"))
        db.session.commit()

        award = Award.query.get(1)

        self.assertEqual(award.name, "Best Artist")
        self.assertEqual(award.year, "2015")

    def test_award_by_name(self):
        db.session.add(Award(name="Best Rock Song", year="2015"))
        db.session.add(Award(name="Best Rock Song", year="2014"))
        db.session.commit()

        awards = Award.query.filter_by(name="Best Rock Song")

        self.assertEqual(len(awards), 2)
        self.assertEqual(awards[0].year, "2015")

    def test_award_not_available(self):
        award = Award.query.filter_by(name="Best Country Song").first()
        self.assertIsNone(award)


if __name__ == '__main__':
    main()