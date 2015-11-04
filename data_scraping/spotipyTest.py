import spotipy
import json
import os
import time
import sys
import requests


def sanitize_jam_base(artist):
    return artist.replace(" ", "+")


if __name__ == '__main__':
    artistFileName = 'artists.json'
    songFileName = 'songs.json'
    releaseFileName = 'releases.json'

    artistJSONList = []
    releaseJSONList = []
    songsJSONList = []

    spotify = spotipy.Spotify()

    for line in sys.stdin:
        results = spotify.search(q='artist:'+line, type='artist')
        artist = results['artists']['items'][0]
        print(artist)
        artistName = artist['name']
        artistJSON = json.dumps({'name': artistName, 'bio': 'Artist BIO HERE', 'large_image': artist['images'][0]['url'],
                                 'medium_image': artist['images'][1]['url'], 'small_image': artist['images'][2]['url'],
                                 'spotify_url': artist['external_urls']['spotify']}, indent=4)
        artistJSONList.append(artistJSON)

        print('\n')
        print('\n')
        # want to change(remove?) album type later to get singles etc but albums only for now
        for release in spotify.artist_albums(results['artists']['items'][0]['id'], album_type='album', country='US')['items']:
            releaseName = release['name']
            releaseJSON = json.dumps({'artist_name':artistName, 'name':releaseName, 'type':release['type'],
                                      'large_image':release['images'][0]['url'], 'medium_image':release['images'][1]['url'],
                                      'small_image':release['images'][2]['url'], 'spotify_url':release['external_urls']['spotify']}, indent=4)
            releaseJSONList.append(releaseJSON)

            #for track in spotify.album_tracks(album['id']):
            #print(track)

            for track in spotify.album_tracks(release['id'])['items']:
                songJSON = json.dumps({'artist_name': artistName, 'release_name': releaseName, 'name': track['name'],
                                       'disc_number': track['disc_number'], 'track_num': track['track_number'],
                                       'other_artists': [artist['name'] for artist in track['artists'] if artist['name'] != artistName],
                                       'spotify_url': track['external_urls']['spotify'], 'preview_url': track['preview_url'],
                                       'duration': track['duration_ms']}, indent=4)
                songsJSONList.append(songJSON)
                print(songJSON)
                print('\n')
            #print(spotify.album_tracks(release['id']))
            print('\n')
            print('\n')
            print(release)
            print('\n')
            print("\n")
            time.sleep(3)
        time.sleep(10)

        #r = requests.get("http://api.jambase.com/artists?name="+sanitize_jam_base(line)+"&page=0&api_key=acb7m44vtfdvnbm2rntpu9ma")

    #UNCOMMENT WHEN YOU WANT TO SAVE THE DATA YOU SCRAPE
    # with open(artistFileName, 'w') as artistFile:
    #     json.dump(artistJSONList, artistFile, indent=4)
    #
    # with open(songFileName, 'w') as songFile:
    #     json.dump(songsJSONList, songFile, indent=4)
    #
    # with open(releaseFileName, 'w') as releaseFile:
    #     json.dump(releaseJSONList, releaseFile, indent=4)

    #print(spotify.artist_albums(results['artists']['items'][0]['id'], album_type='album'))