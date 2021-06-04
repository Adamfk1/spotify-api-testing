import json
import requests
from secrets import spotify_user_id
from pip._vendor.urllib3 import response

class Playlist:
    def __init__(self):
        self.spotify_user_id = spotify_user_id
        self.spotify_access_token = ""
        self.playlist_id = ""
        self.tracks = []

    def create_playlist(self):

        name = input("Playlist name: ")
        desc = input("Playlist desc: ")


        """Create A New Playlist"""
        request_body = json.dumps({
            "name": name,
            "description": desc,
            "public": True
        })
        
        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)


        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_access_token)
            }
        )
        playlist_json = response.json()

        print("Playlist created!")

        self.playlist_id = playlist_json["id"]

        return playlist_json["id"]



    def find_songs(self):
        
        self.search_for_track = input("Search for a song: ")

        query = "https://api.spotify.com/v1/search?q={}&type=track&market=US&limit=5".format(self.search_for_track)

        response = requests.get(query, headers={"Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_access_token)})

        tracks_json = response.json()

        print(tracks_json['tracks']['items'][1]['uri'])

        for i in range(4):
            current_track = tracks_json['tracks']['items'][i]['name']

            print("Track:", i+1, current_track)

            self.tracks.append(tracks_json['tracks']['items'][i]['uri'])

        return self.tracks

    def add_to_playlist(self):

        print("Adding songs.")

        for track in self.tracks:

            query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.playlist_id, track)

            response = requests.post(query, headers={"Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_access_token)})

        print(response.json)









