import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

class SpotifyTopChart:

    def __init__(self):
        SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
        SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

        client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_top_50_chart(self, country):
        # country = "Italy"
        # country = 'UK'
        # country = 'Germany'
        # country = 'Sweden'
        # country = 'Norway'
        # country = 'France'
        response = self.sp.search(f"TOP 50 {country}", type='playlist')
        top_country_playlist = response['playlists']['items'][0]
        results = self.sp.user_playlist('spotify', top_country_playlist['id'], fields="tracks,next")
        tracks = results['tracks']

        result = []
        for i, item in enumerate(tracks['items']):
            track = item['track']
            # print("   %d %32.32s - %s" % (i+1, track['artists'][0]['name'], track['name']))

            result.append("   %d %32.32s - %s" % (i+1, track['artists'][0]['name'], track['name']))

        return result
