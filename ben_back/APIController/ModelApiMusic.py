import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#Doc : https://developer.spotify.com/documentation/web-api

class ModelApiMusic:
    def __init__(self, client_id, client_secret, redirect_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_url

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope="user-library-read user-read-playback-state user-modify-playback-state"
        ))
    
    def search_and_play(self, track_name):
        results = self.sp.search(q=track_name, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_uri = track['uri']
            
            devices = self.sp.devices()
            if devices['devices']:
                device_id = devices['devices'][0]['id'] 
                self.sp.start_playback(device_id=device_id, uris=[track_uri])
                return f"Lecture du morceau: {track['name']} par {track['artists'][0]['name']}"
            else:
                return "Aucun appareil connecté pour la lecture"
        else:
            return "Aucun morceau trouvé"