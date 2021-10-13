import os
from spotifyclient import SpotifyClient

def main():
    # tok = "BQB5hH9N98VIs4p6FHLO7sxZikUCt-67c0ZUn1jcU3i3-A6any5w1vaMmfK1TczZvEtd7x7NfC0RpLtAUgAfP5r1B7UAX_LV78oOy7vgOC5tsTjTrlI6Yi0E0YtPznHGQKA44860eQV27m2F-awzw3zPvNCPBjQcdEBVN9LlIMR4W9SgPPdLRoD81l2E7cUvAJh4YvEfJWUj4oaoV_EuepJ-xW4qUR9or6TrC__3eExSMjh3"
    # usrid = "BQBrhf5CKe8OoWsiMg-ISO-3jvyaTaVUvmuUz5ch28y5p4ajtbex5T3Sv4Rnxzq0k-ezYnBegneyw8Ygp-fImAsecuhXliDMLN7xMyIkKBVpaA1ENcofr5FyKP_ass9gsiqGkxFk978eJCXHuM_CPM6G4AntE8MOBU6PtFe0TpL9V7v-V8RdgeUZHFNHxNiG30eB-inMrKQ9YMqJLWtE0xbP7WVfmPddVQwlPgXEXsi1wsCl"
    #instantiate spotify client
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"), os.getenv("SPOTIFY_USER_ID"))
    # spotify_client = SpotifyClient(tok, usrid)

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