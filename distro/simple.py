import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate_spotify():
    # Set your Spotify API credentials
    client_id = '894d0857540740438d1ef159b85774bc'
    client_secret = '7b92c99a70c245299dd709e4ec59ea46'
    redirect_uri = 'https://www.example.com/succses'

    # Set the necessary scope (e.g., user-read-playback-state, user-modify-playback-state)
    scope = 'user-read-playback-state,user-modify-playback-state'

    # Create a Spotify OAuth object
    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

    # Get the token
    token_info = sp_oauth.get_cached_token()

    # If token is not present or expired, get a new one
    if not token_info or sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.get_access_token()
    
    return token_info['access_token']

def play_track(sp, track_uri):
    sp.start_playback(uris=[track_uri])

def main():
    # Authenticate with Spotify
    access_token = authenticate_spotify()

    # Create a Spotipy instance
    sp = spotipy.Spotify(auth=access_token)

    # Get a track URI (replace with your desired track URI)
    track_uri = 'spotify:track:4iV5W9uYEdYUVa79Axb7Rh'

    # Play the track
    play_track(sp, track_uri)

if __name__ == "__main__":
    main()
