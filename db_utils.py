import csv
import json
import os
from sqlalchemy.exc import SQLAlchemyError
from flask_app import db
from flask_app.main.models import Artist, Award, Concert, Label, Release, Song, ArtistRelease


def recreate_db():
    try:
        db.reflect()
        db.drop_all()
    except SQLAlchemyError as e:
        raise ValueError(e)

    db.create_all()

    db.session.commit()


def _map_csv_to_list_of_dicts(filename):
    current_path = os.path.dirname(__file__)
    csv_path = os.path.join(current_path, 'db_setup', filename)

    dicts = []

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column_headers = []
        for row in reader:
            if len(column_headers) is 0:
                column_headers = row
            else:
                col_num = 0
                csv_row_as_dict = {}
                for column_header in column_headers:
                    try:
                        csv_row_as_dict[column_header] = row[col_num]
                    except IndexError as e:
                        pass
                    col_num += 1

                dicts.append(csv_row_as_dict)

    return dicts


def _map_dict_to_object(dict_to_map, obj):
    for key in dict_to_map:
        value = dict_to_map[key]
        if value is not None and value != '':
            setattr(obj, key, dict_to_map[key])


def _seed_csv_artists():
    csv_filename = 'seed_data/artists.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for artist_dict in dicts:
        artist = Artist()
        _map_dict_to_object(artist_dict, artist)
        db.session.add(artist)


def _seed_csv_awards():
    csv_filename = 'seed_data/awards.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for award_dict in dicts:
        award = Award()
        _map_dict_to_object(award_dict, award)
        db.session.add(award)


def _seed_csv_concerts():
    csv_filename = 'seed_data/concerts.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for concerts_dict in dicts:
        concerts = Concert()
        _map_dict_to_object(concerts_dict, concerts)
        db.session.add(concerts)


def _seed_csv_labels():
    csv_filename = 'seed_data/labels.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for labels_dict in dicts:
        labels = Label()
        _map_dict_to_object(labels_dict, labels)
        db.session.add(labels)


def _seed_csv_releases():
    csv_filename = 'seed_data/releases.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for releases_dict in dicts:
        releases = Release()
        _map_dict_to_object(releases_dict, releases)
        db.session.add(releases)


def _seed_csv_songs():
    csv_filename = 'seed_data/songs.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for songs_dict in dicts:
        songs = Song()
        _map_dict_to_object(songs_dict, songs)
        db.session.add(songs)


# def _seed_csv_videos():
#     csv_filename = 'seed_data/videos.csv'
#     dicts = _map_csv_to_list_of_dicts(csv_filename)
#
#     for videos_dict in dicts:
#         videos = Video()
#         _map_dict_to_object(videos_dict, videos)
#         db.session.add(videos)

def _get_generator_json_objs(filename):
    current_path = os.path.dirname(__file__)
    json_path = os.path.join(current_path, filename)
    with open(json_path, 'r') as json_file:
        objs = json.load(json_file)
        for obj in objs:
            yield json.loads(obj)


def _seed_json_artists():
    json_filename = 'data_scraping/artists.json'
    #i = 1
    for artistJSON in _get_generator_json_objs(json_filename):
        artist = Artist()
        for key, value in artistJSON.items():
            setattr(artist, key, value)
        #setattr(artist, 'id', i)
        #i += 1
        db.session.add(artist)


def _seed_json_releases():
    json_filename = 'data_scraping/releases.json'
    unusedFieldsFilter = {'artist_name'}
    #i = 1
    for releaseJSON in _get_generator_json_objs(json_filename):
        release = Release()
        #artist_ids = []
        artist = Artist.query.filter_by(name=releaseJSON['artist_name']).first()
        #print(artist.id)
        #setattr(release, 'id', i)
        for key, value in releaseJSON.items():
            if key not in unusedFieldsFilter:
                setattr(release, key, value)

        release.artists.append(artist)
        db.session.add(release)

def _seed_json_songs():
    json_filename = 'data_scraping/songs.json'
    unusedFieldsFilter = {'artist_name', 'release_name', 'other_artists'}
    for songJSON in _get_generator_json_objs(json_filename):
        song = Song()
        #artist = Artist.query.filter_by(name=songJSON['artist_name']).first()
        #Do basic querying for now. We know dataset doesn't contain conflicting names
        release = Release.query.filter_by(name=songJSON['release_name']).first()
        for key, value in songJSON.items():
            if key not in unusedFieldsFilter:
                setattr(song, key, value)
        song.releases.append(release)
        db.session.add(song)

def _seed_json_labels():
    json_filename = 'data_scraping/labels.json'
    unusedFieldsFilter = {'artists'}
    for labelJSON in _get_generator_json_objs(json_filename):
        label = Label()
        for artistName in labelJSON['artists']:
            artist = Artist.query.filter_by(name=artistName).first()
            label.artists.append(artist)
        for key, value in labelJSON.items():
            if key not in unusedFieldsFilter:
                setattr(label, key, value)
        db.session.add(label)
def _test_linking_tables():

    for i in range(1, 15):
        query = ArtistRelease.query.get(i)
        print(str(query.artist_id) + " " + str(query.release_id))




def seed_database_prod():
    _seed_json_artists()
    _seed_json_releases()
    _seed_json_songs()
    _seed_json_labels()
    db.session.commit()
    #_test_linking_tables()

def seed_database_dev():
    #_seed_csv_videos()
    _seed_csv_songs()
    _seed_csv_releases()
    _seed_csv_labels()
    _seed_csv_concerts()
    _seed_csv_awards()
    _seed_csv_artists()

    db.session.commit()


