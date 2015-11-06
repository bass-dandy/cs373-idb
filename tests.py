import json
from unittest import main, TestCase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask_app.main.models import *

class Test(TestCase):
    def setUp(self):
        print("setup")
        engine = create_engine("postgresql://musicmecca:mecca@localhost/musicmecca", echo=False)
        self.session = sessionmaker
        self.session.configure(bind=engine)

    def test_artist_id(self):
        artist = self.session.query(Artist).get(1)
        self.assertEqual("Chon", artist['name'])
        print("Artist Test 1\nExpected: Chon\nActual: "+artist['name'])