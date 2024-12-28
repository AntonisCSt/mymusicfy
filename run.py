from src.mymusicfy import MyMusicFy
from src.utils import (
#fill this the way you like
)

# Initialize MyMusicFy with the path to your data
mymusicfy = MyMusicFy()

# Fetch stats for a specific artist (replace 'Adele' with any artist name)
artist_stats = mymusicfy.get_artist_stats("Adele")
print(format_artist_stats(artist_stats))

# Fetch genre stats (this will show average popularity for each genre)
genre_stats = mymusicfy.get_genre_stats()
print(format_genre_stats(genre_stats))

# Get the average number of tracks per album
avg_tracks = mymusicfy.get_average_tracks_per_album()
print(f"Average tracks per album: {avg_tracks}")
