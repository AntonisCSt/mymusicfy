def format_artist_stats(stats: dict) -> str:
    """
    Format artist statistics into a readable string.
    :param stats: Dictionary containing artist statistics.
    :return: Formatted string.
    """
    if "error" in stats:
        return stats["error"]

    return (
        f"Artist: {stats['name']}\n"
        f"Followers: {stats['followers']}\n"
        f"Popularity: {stats['popularity']}\n"
        f"Main Genre: {stats['main_genre']}\n"
        f"Total Albums: {stats['total_albums']}\n"
        f"Total Songs: {stats['total_songs']}"
    )

def format_genre_stats(genre_stats: dict) -> str:
    """
    Format genre-based statistics into a readable string.
    :param genre_stats: Dictionary containing genre statistics.
    :return: Formatted string.
    """
    sorted_genres = sorted(genre_stats.items(), key=lambda x: x[1], reverse=True)[:10]
    return "\n".join(f"{genre}: {popularity:.2f}" for genre, popularity in sorted_genres)

def format_song_explicitness(explicit_stats: dict) -> str:
    """
    Format song explicitness stats into a readable string.
    :param explicit_stats: Dictionary containing explicit and non-explicit song counts.
    :return: Formatted string.
    """
    return (
        f"Explicit Songs: {explicit_stats['explicit']}\n"
        f"Non-Explicit Songs: {explicit_stats['non_explicit']}"
    )
