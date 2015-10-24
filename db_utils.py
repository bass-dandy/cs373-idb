import csv
import os
from sqlalchemy.exc import SQLAlchemyError
from flask.ext.app import db
from flask.ext.app.main.models import Artist, Award


def recreate_db():
    try:
        db.reflect()
        db.drop_all()
    except SQLAlchemyError:
        pass

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
    csv_filename = '/seed_data/artists.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for artist_dict in dicts:
        artist = Artist()
        _map_dict_to_object(artist_dict, artist)
        db.session.add(artist)


def _seed_csv_awards():
    csv_filename = '/seed_data/awards.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for award_dict in dicts:
        award = Award()
        _map_dict_to_object(award_dict, award)
        db.session.add(award)


def _seed_csv_concerts():
    csv_filename = '/seed_data/concerts.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for concerts_dict in dicts:
        concerts = Artist()
        _map_dict_to_object(concerts_dict, concerts)
        db.session.add(concerts)


def _seed_csv_labels():
    csv_filename = '/seed_data/labels.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for labels_dict in dicts:
        labels = Artist()
        _map_dict_to_object(labels_dict, labels)
        db.session.add(labels)


def _seed_csv_releases():
    csv_filename = '/seed_data/releases.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for releases_dict in dicts:
        releases = Artist()
        _map_dict_to_object(releases_dict, releases)
        db.session.add(releases)


def _seed_csv_songs():
    csv_filename = '/seed_data/songs.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for songs_dict in dicts:
        songs = Artist()
        _map_dict_to_object(songs_dict, songs)
        db.session.add(songs)


def _seed_csv_videos():
    csv_filename = '/seed_data/videos.csv'
    dicts = _map_csv_to_list_of_dicts(csv_filename)

    for videos_dict in dicts:
        videos = Artist()
        _map_dict_to_object(videos_dict, videos)
        db.session.add(videos)


def seed_database_dev():
    _seed_csv_videos()
    _seed_csv_songs()
    _seed_csv_releases()
    _seed_csv_labels()
    _seed_csv_concerts()
    _seed_csv_awards()
    _seed_csv_artists()


def reset_postgres_id_sequences():
    tables = ['artists', 'awards', 'concerts', 'labels', 'releases', 'songs', 'videos']

    for table in tables:
        sql = "SELECT setval('{0}_id_seq', MAX(id)) FROM {0};".format(table)
        db.engine.execute(sql)

