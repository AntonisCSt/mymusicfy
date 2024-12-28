from src.mymusicfy import MyMusicFy
from src.utils import (
    format_artist_stats,
    format_genre_stats,
    format_song_explicitness,
)

# Initialize MyMusicFy with the path to your data
mymusicfy = MyMusicFy()

# Fetch stats for a specific artist (replace 'Adele' with any artist name)
artist_stats = mymusicfy.get_artist_stats("Adele")
print(format_artist_stats(artist_stats))

# Fetch genre stats (this will show average popularity for each genre)
genre_stats = mymusicfy.get_genre_stats()
print(format_genre_stats(genre_stats))

# Fetch the distribution of explicit vs. non-explicit songs
explicit_stats = mymusicfy.get_song_explicitness_distribution()
print(format_song_explicitness(explicit_stats))

# Get the average number of tracks per album
avg_tracks = mymusicfy.get_average_tracks_per_album()
print(f"Average tracks per album: {avg_tracks}")
