import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import requests
from secrets import spotify_user_id
from refresh import Refresh
from playlist import Playlist
from pip._vendor.urllib3 import response

class Spot:
    def __init__(self):
        self.spotify_user_id = spotify_user_id
        self.spotify_access_token = ""
        self.playlist_id = ""
        self.tracks = []

    def start(self):
        pass

    def get_token(self):
        print("Refreshing token...")

        refreshCaller = Refresh()
        self.spotify_access_token = refreshCaller.refresh()
        
        self.playlist_id = Playlist.create_playlist(self)

        self.tracks = Playlist.find_songs(self)

        Playlist.add_to_playlist(self)

        print("Playlist created!")

        



a = Spot()
a.get_token()
