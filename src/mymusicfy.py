import pandas as pd

data_dir = "src/data"

artists = pd.read_csv(f"{data_dir}/artists.csv", sep='\t')
albums = pd.read_csv(f"{data_dir}/albums.csv", sep='\t')
releases = pd.read_csv(f"{data_dir}/releases.csv", sep='\t')
songs = pd.read_csv(f"{data_dir}/songs.csv", sep='\t')
tracks = pd.read_csv(f"{data_dir}/tracks.csv", sep='\t')

# Retrieve statistics for a specific artist.
artist_name = 'Kanye west'

artist_data = artists[artists["name"].str.lower() == artist_name.lower()]

if artist_data.empty:
    print("ERROR: Artist not found")
else:
      
    artist_info = artist_data.iloc[0]
    albums = albums[albums["artists"].str.contains(artist_name, case=False)]
    songs = songs[songs["artists"].str.contains(artist_name, case=False)]

    print({
            "name": artist_info["name"],
            "followers": artist_info["followers"],
            "popularity": artist_info["popularity"],
            "main_genre": artist_info["main_genre"],
            "total_albums": len(albums),
            "total_songs": len(songs),
        })


# Retrieve genre-based statistics, including most popular artists and albums.
genre_popularity = artists.groupby("main_genre")["popularity"].mean().sort_values(ascending=False).head()
print(genre_popularity.to_dict())   


# Retrieve the top N albums based on popularity.
top_n = 10

print(f"\n Top {top_n} albums based on popularity:")
top_albums = albums.nlargest(top_n, "total_tracks")[["name", "artists", "total_tracks"]]
print( top_albums.to_dict(orient="records"))


# Calculate the average number of tracks per album.

if albums.empty:
    average_tracks = 0.0
else:
# Calculate the average, handling potential NaN values
    average_tracks = albums["total_tracks"].dropna().mean()

print(f"\n Average_tracks = {average_tracks}")
    
    
