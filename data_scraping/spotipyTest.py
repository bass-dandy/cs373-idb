import spotipy
import json
import os
import time
import sys
import requests
import discogs_client

class Label:
    def __init__(self):
        self.name = ""
        self.small_image = ""
        self.bio = ""
        self.artists = []

def sanitize_jam_base(artist):
    return artist.replace(" ", "+")


def add_artist(label, artist_name):
    # print(type(label_json))
    label.artists.append(artist_name)

def build_label(label, label_name, artist_name):
    tempLabel = Label()
    tempLabel.name = label_name
    tempLabel.bio = label_name + " bio goes here"
    tempLabel.artists.append(artist_name)
    if label.images is not None:
        if len(label.images) != 0:
            tempLabel.small_image = label.images[0]['uri']
    # if label.profile is not None:
    #	bio = label.profile
    return tempLabel


if __name__ == '__main__':
    artistFileName = 'artists.json'
    songFileName = 'songs.json'
    releaseFileName = 'releases.json'
    labelFileName = 'labels.json'

    artistJSONList = []
    releaseJSONDict = {}
    songsJSONList = []
    labelsJSONDict = {}

    first_release = True
    current_artist = ''
    spotify = spotipy.Spotify()
    discogs = discogs_client.Client('MusicMeccaTest/0.1', user_token="zpuXwiGndCevtSgOIcMzuRuadcQTdQWZSGltErYH")
    artistFound = True
    for line in sys.stdin:
        results = spotify.search(q='artist:' + line, type='artist')

        if len(results['artists']['items']) != 0:
            artist = results['artists']['items'][0]
            print(artist)
            artistName = artist['name']
            artistJSON = json.dumps(
                {'name': artistName, 'bio': 'Artist BIO HERE', 'large_image': artist['images'][0]['url'],
                 'medium_image': artist['images'][1]['url'], 'small_image': artist['images'][2]['url'],
                 'spotify_url': artist['external_urls']['spotify']}, indent=4)
            artistJSONList.append(artistJSON)

            print('\n')
            print('\n')

            first_release = True


            # want to change(remove?) album type later to get singles etc but albums only for now
            for release in spotify.artist_albums(results['artists']['items'][0]['id'], album_type='album', country='US')[
                'items']:
                releaseName = release['name']

                if releaseName not in releaseJSONDict:

                    tracks = spotify.album_tracks(release['id'])['items']

                    # #get label info
                    if current_artist != artistName:
                        first_release = True
                        current_artist = artistName
                    if first_release:
                        results = discogs.search(releaseName, type="master", release_title=releaseName,
                                           artist=current_artist)
                        for r in results:
                            time.sleep(5)
                            # print(r)
                            if type(r) is discogs_client.Master and r.main_release.title == releaseName and first_release:
                                #print("MASTER^")
                                # print(r.main_release.labels[0].images)
                                # print(r.main_release.labels[0].name)
                                if len(r.main_release.labels) != 0:
                                    label = r.main_release.labels[0]
                                    if label is not None:
                                        # print(label.images)
                                        print(label.name)
                                        labelName = label.name
                                        if labelName.endswith(')'):
                                            # print(labelName.endswith(')'))
                                            index = labelName.rfind(' ')
                                            # print(index)
                                            # print(r.main_release.labels[0].name[0:index])
                                            labelName = labelName[0:index]
                                        # print(r.main_release.title)
                                        if labelName in labelsJSONDict:
                                            add_artist(labelsJSONDict[labelName], current_artist)
                                        else:
                                            labelsJSONDict[labelName] = build_label(label, labelName, current_artist)
                                        first_release = False

                    releaseJSON = json.dumps({'artist_name': artistName, 'name': releaseName, 'type': release['type'],
                                              'large_image': release['images'][0]['url'],
                                              'medium_image': release['images'][1]['url'],
                                              'small_image': release['images'][2]['url'],
                                              'spotify_url': release['external_urls']['spotify']}, indent=4)
                    releaseJSONDict[releaseName] = releaseJSON


                    # for track in spotify.album_tracks(album['id']):
                    # print(track)
                    tracks = spotify.album_tracks(release['id'])['items']
                    for track in tracks:
                        songJSON = json.dumps({'artist_name': artistName, 'release_name': releaseName, 'name': track['name'],
                                               'disc_number': track['disc_number'], 'track_num': track['track_number'],
                                               'other_artists': [artist['name'] for artist in track['artists'] if
                                                                 artist['name'] != artistName],
                                               'spotify_url': track['external_urls']['spotify'],
                                               'preview_url': track['preview_url'],
                                               'duration': track['duration_ms']}, indent=4)
                        songsJSONList.append(songJSON)
                        print(songJSON)
                        print('\n')
                    if len(tracks) == 0:
                        print("EMPTY TRACKS")
                        releaseJSONList.pop()
                    # print(spotify.album_tracks(release['id']))
                    print('\n')
                    print('\n')
                    print(release)
                    print('\n')
                    print("\n")
                    time.sleep(3)
            time.sleep(10)
        else:
            print(line + " not found")

        # r = requests.get("http://api.jambase.com/artists?name="+sanitize_jam_base(line)+"&page=0&api_key=acb7m44vtfdvnbm2rntpu9ma")

        # UNCOMMENT WHEN YOU WANT TO SAVE THE DATA YOU SCRAPE
    with open(artistFileName, 'w') as artistFile:
        json.dump(artistJSONList, artistFile, indent=4)

    with open(songFileName, 'w') as songFile:
        json.dump(songsJSONList, songFile, indent=4)

    with open(releaseFileName, 'w') as releaseFile:
        json.dump([releaseobj for releaseobj in releaseJSONDict.values()], releaseFile, indent=4)

    with open(labelFileName, 'w') as labelFile:
        json.dump([json.dumps({'name': label.name, 'artists': label.artists, 'small_image': label.small_image, 'bio': label.bio}, indent=4) for label in labelsJSONDict.values()], labelFile, indent=4)

        # print(spotify.artist_albums(results['artists']['items'][0]['id'], album_type='album'))
