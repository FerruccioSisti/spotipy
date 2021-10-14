import os
from spotifyclient import SpotifyClient

def main():
    #instantiate spotify client
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"), os.getenv("SPOTIFY_USER_ID"))

    #get last played tracks
    num_tracks_to_visualize = int((input("How many tracks would you like to visualize/take data from?")))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualize)

    print(f"Here are the last {num_tracks_to_visualize} tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index+1}- {track}")
    
    #choose which tracks you want to use as a seed to generate a new playlist
    indexes = input("Enter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated byu a space:")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]

    #get recommended tracks based off seed tracks
    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("Here are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")

    #get playlist name from user and then create the playlist
    playlist_name = input("What's the playlist's name? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"{playlist.name} was created successfully")

    #populate the new playlist with recommended tracks
    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"Recommended tracks successfully uploaded to playlist '{playlist.name}'")

if __name__ == "__main__":
    main()