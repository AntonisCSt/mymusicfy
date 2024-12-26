import pandas as pd


class MyMusicFy:
    def __init__(self):
        """
        Initialize the MyMusicFy class with the directory containing metadata files.
        :param data_dir: Path to the folder containing the metadata CSV files.
        """
        data_dir = "src/data"
        self.artists = pd.read_csv(f"{data_dir}/artists.csv", sep='\t')
        self.albums = pd.read_csv(f"{data_dir}/albums.csv", sep='\t')
        self.releases = pd.read_csv(f"{data_dir}/releases.csv", sep='\t')
        self.songs = pd.read_csv(f"{data_dir}/songs.csv", sep='\t')
        self.tracks = pd.read_csv(f"{data_dir}/tracks.csv", sep='\t')

    def get_artist_stats(self, artist_name: str) -> dict:
        """
        Retrieve statistics for a specific artist.
        :param artist_name: Name of the artist.
        :return: A dictionary containing artist stats.
        """
        artist_data = self.artists[self.artists["name"].str.lower() == artist_name.lower()]
        if artist_data.empty:
            return {"error": "Artist not found"}

        artist_info = artist_data.iloc[0]
        albums = self.albums[self.albums["artists"].str.contains(artist_name, case=False)]
        songs = self.songs[self.songs["artists"].str.contains(artist_name, case=False)]

        return {
            "name": artist_info["name"],
            "followers": artist_info["followers"],
            "popularity": artist_info["popularity"],
            "main_genre": artist_info["main_genre"],
            "total_albums": len(albums),
            "total_songs": len(songs),
        }

    def get_genre_stats(self) -> dict:
        """
        Retrieve genre-based statistics, including most popular artists and albums.
        :return: A dictionary of genre stats.
        """
        genre_popularity = self.artists.groupby("main_genre")["popularity"].mean().sort_values(ascending=False)
        return genre_popularity.to_dict()

    def get_top_albums(self, top_n: int = 10) -> list:
        """
        Retrieve the top N albums based on popularity.
        :param top_n: Number of top albums to retrieve.
        :return: A list of top albums.
        """
        top_albums = self.albums.nlargest(top_n, "total_tracks")[["name", "artists", "total_tracks"]]
        return top_albums.to_dict(orient="records")

    def get_song_explicitness_distribution(self) -> dict:
        """
        Retrieve the distribution of explicit vs. non-explicit songs.
        :return: A dictionary with counts of explicit and non-explicit songs.
        """
        explicit_distribution = self.songs["explicit"].value_counts().to_dict()
        return {
            "explicit": explicit_distribution.get(True, 0),
            "non_explicit": explicit_distribution.get(False, 0),
        }

    def get_average_tracks_per_album(self) -> float:
        """
        Calculate the average number of tracks per album.
        :return: The average number of tracks per album.
        """
        return self.albums["total_tracks"].mean()
