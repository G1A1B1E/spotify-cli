import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException

def authenticate_spotify():
    client_id = '894d0857540740438d1ef159b85774bc'
    client_secret = '7b92c99a70c245299dd709e4ec59ea46'
    redirect_uri = 'https://www.example.com/succses'
    scope = 'user-read-playback-state,user-modify-playback-state'
    
    try:
        sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
        token_info = sp_oauth.get_cached_token()

        if not token_info or sp_oauth.is_token_expired(token_info):
            token_info = sp_oauth.get_access_token()

        return token_info['access_token']
    except SpotifyException as e:
        print(f"Authentication failed: {str(e)}")
        return None

def search_track(sp, query):
    try:
        results = sp.search(q=query, type='track', limit=1)

        if results['tracks']['items']:
            return results['tracks']['items'][0]['uri']
        else:
            print(f"Song not found: {query}")
            return None
    except SpotifyException as e:
        print(f"Error during track search: {str(e)}")
        return None

def play_track(sp, track_uri):
    try:
        sp.start_playback(uris=[track_uri])
        print(f"Playing: {sp.track(track_uri)['name']} by {', '.join([artist['name'] for artist in sp.track(track_uri)['artists']])}")
    except SpotifyException as e:
        print(f"Error during playback: {str(e)}")

def main():
    access_token = authenticate_spotify()

    if not access_token:
        return

    sp = spotipy.Spotify(auth=access_token)
    
    while True:
        query = input("Enter the name of a song (type 'exit' to quit): ")
        
        if query.lower() == 'exit':
            break
        
        if not query:
            print("Please enter a valid song name.")
            continue

        track_uri = search_track(sp, query)
        
        if track_uri:
            play_track(sp, track_uri)

if __name__ == "__main__":
    main()
