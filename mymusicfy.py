import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
artists = pd.read_csv("./artists.csv", sep='\t')
albums = pd.read_csv("./albums.csv", sep='\t')
releases = pd.read_csv("./releases.csv", sep='\t')
songs = pd.read_csv("./songs.csv", sep='\t')
tracks = pd.read_csv("./tracks.csv", sep='\t')

# Retrieve statistics for a specific artist
artist_name = 'Kanye West'

artist_data = artists[artists["name"].str.lower() == artist_name.lower()]

if artist_data.empty:
    print("ERROR: Artist not found.")
else:
    artist_info = artist_data.iloc[0]
    artist_albums = albums[albums["artists"].str.contains(artist_name, case=False)]
    artist_songs = songs[songs["artists"].str.contains(artist_name, case=False)]

    print("\n=== Artist Statistics ===")
    print(f"Name: {artist_info['name']}")
    print(f"Followers: {artist_info['followers']}")
    print(f"Popularity: {artist_info['popularity']}")
    print(f"Main Genre: {artist_info['main_genre']}")
    print(f"Total Albums: {len(artist_albums)}")
    print(f"Total Songs: {len(artist_songs)}")

# Retrieve genre-based statistics
genre_popularity = artists.groupby("main_genre")["popularity"].mean().sort_values(ascending=False).head()
print("\n=== Top Genres by Average Popularity ===")
for genre, popularity in genre_popularity.items():
    print(f"{genre}: {popularity:.2f}")

# Retrieve the top N albums based on popularity
top_n = 10
top_albums = albums.nlargest(top_n, "total_tracks")[["name", "artists", "total_tracks"]]

print(f"\n=== Top {top_n} Albums by Total Tracks ===")
for idx, row in top_albums.iterrows():
    print(f"Album: {row['name']}")
    print(f"Artists: {row['artists']}")
    print(f"Total Tracks: {row['total_tracks']}")
    print("-" * 40)

# Calculate the average number of tracks per album
if albums.empty:
    average_tracks = 0.0
else:
    average_tracks = albums["total_tracks"].dropna().mean()

print(f"\n=== Average Number of Tracks Per Album ===")
print(f"Average Tracks: {average_tracks:.2f}")

# Visualization Section
print("\nGenerating visualizations...")

# 1. Top Genres by Popularity (Bar Plot)
plt.figure(figsize=(8, 6))
sns.barplot(x=genre_popularity.values, y=genre_popularity.index, palette="viridis")
plt.title("Top Genres by Average Popularity", fontsize=16)
plt.xlabel("Average Popularity", fontsize=12)
plt.ylabel("Genre", fontsize=12)
plt.tight_layout()
plt.savefig("top_genres_by_popularity.jpg", format="jpg")
plt.close()

# 2. Distribution of Album Track Counts (Histogram)
plt.figure(figsize=(8, 6))
sns.histplot(albums["total_tracks"].dropna(), bins=20, kde=True, color="blue")
plt.title("Distribution of Album Track Counts", fontsize=16)
plt.xlabel("Number of Tracks", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.tight_layout()
plt.savefig("album_track_distribution.jpg", format="jpg")
plt.close()

# 3. Artist Popularity vs Followers (Scatter Plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=artists["followers"], y=artists["popularity"], hue=artists["main_genre"], palette="muted", alpha=0.7)
plt.title("Artist Popularity vs Followers", fontsize=16)
plt.xlabel("Followers", fontsize=12)
plt.ylabel("Popularity", fontsize=12)
plt.legend(title="Main Genre", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("artist_popularity_vs_followers.jpg", format="jpg")
plt.close()

print("Visualizations have been saved as JPG files in the current directory.")
