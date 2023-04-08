import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

################## SpotifyPKCE
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-library-read streaming user-read-playback-state"))

import ipdb; ipdb.set_trace()
sp.current_user_playing_track()
# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'],   playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None



# ################## With user authentication
# ################## https://pypi.org/project/spotipy/
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
#                                                client_secret=SPOTIPY_CLIENT_SECRET,
#                                                redirect_uri=SPOTIPY_REDIRECT_URI,
#                                                scope="user-library-read"))
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " - ", track['name'])


# ################## Authorization Code Flow
# ################## https://spotipy.readthedocs.io/en/2.16.1/#getting-started
# scope = "user-library-read" # https://developer.spotify.com/documentation/web-api/concepts/scopes
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
#                                                client_id=SPOTIPY_CLIENT_ID,
#                                                client_secret=SPOTIPY_CLIENT_SECRET,
#                                                redirect_uri=SPOTIPY_REDIRECT_URI))
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " - ", track['name'])


# ################# Client Credentials Flow
# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)
# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None

