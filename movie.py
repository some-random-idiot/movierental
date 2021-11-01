class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, year, genre):
        """Initialize a new movie."""
        self._title = title
        self._year = year
        self._genre = genre

    def get_title(self):
        """Get the title of this movie"""
        return self._title

    def get_year(self):
        return self._year

    def get_genre_list(self):
        return self._genre

    def is_genre(self, string):
        return string in self._genre

    def __str__(self):
        return self._title
