import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate_spotify():
    client_id = '894d0857540740438d1ef159b85774bc'
    client_secret = '7b92c99a70c245299dd709e4ec59ea46'
    redirect_uri = 'https://www.example.com/succses'
    scope = 'user-read-playback-state,user-modify-playback-state'
    
    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
    
    token_info = sp_oauth.get_cached_token()
    
    if not token_info or sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.get_access_token()
    
    return token_info['access_token']

def search_track(sp, query):
    results = sp.search(q=query, type='track', limit=1)
    
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    
    return None

def play_track(sp, track_uri):
    sp.start_playback(uris=[track_uri])

def main():
    access_token = authenticate_spotify()
    sp = spotipy.Spotify(auth=access_token)
    
    while True:
        query = input("Enter the name of a song (type 'exit' to quit): ")
        
        if query.lower() == 'exit':
            break
        
        track_uri = search_track(sp, query)
        
        if track_uri:
            print(f"Playing: {query}")
            play_track(sp, track_uri)
        else:
            print(f"Song not found: {query}")

if __name__ == "__main__":
    main()
