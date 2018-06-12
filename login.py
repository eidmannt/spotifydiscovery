# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy.util as util
#
#
# cid ="576665c63aa04da1a8f2a359ef5c43d3"
# secret = "ae671197233541b693ca6c9e776e201f"
# username = ""
# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# scope = 'user-library-read playlist-read-private'
# token = util.prompt_for_user_token(username, scope)
# if token:
#     sp = spotipy.Spotify(auth=token)
# else:
#     print("Can't get token for", username)

import configparser

import spotipy
import spotipy.oauth2 as oauth2

config = configparser.ConfigParser()
config.read('config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')


auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)
