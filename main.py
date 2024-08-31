import requests
from datetime import datetime
from pprint import pprint
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

#date = input("Which date would you like to look at?")
#response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
#response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-12-12")

#soup = BeautifulSoup(response.text)

#song_names_spans = soup.select("li ul li h3")
#song_names = [song.getText().strip() for song in song_names_spans]



CLIENT_ID="1d8289f48a514ac29c50da2b22ad7498"
CLIENT_secret="0a0c49ab9e314f57b7cfefcfb734419c"

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_secret,redirect_uri="localost:3000", scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
