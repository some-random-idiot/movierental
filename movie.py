import csv


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: str, genre: list):
        """Initialize a new movie."""
        self.__title = title
        self.__year = year
        self.__genre = genre

    def get_title(self) -> str:
        """Get the title of this movie"""
        return self.__title

    def get_year(self) -> str:
        """Get the year that this movie was released in."""
        return self.__year

    def get_genre_list(self) -> list:
        """Get a list of genre(s) this movie belongs to."""
        return self.__genre

    def is_genre(self, string: str) -> bool:
        """Check if this movie belongs to the provided 'string' parameter"""
        return string in self.__genre

    def __str__(self):
        return self.__title


class MovieCatalog:
    """A movie catalog containing various movies."""

    def __init__(self):
        """Initializes a new MovieCatalog."""
        self.catalog = {}
        self.last_index = 0

    def add_movie(self):
        """Add a movie from a csv file to the catalog."""
        with open('movies.csv', 'r') as f:
            rows = list(csv.reader(f))
            self.catalog[rows[self.last_index][1]] = Movie(rows[self.last_index][1], rows[self.last_index][2],
                                                           rows[self.last_index][3].split(sep='|'))
        self.last_index += 1

    def get_movie(self, title: str) -> Movie:
        """Get a movie object from the catalog."""
        while True:
            if title in self.catalog:
                return self.catalog[title]
            else:
                try:
                    self.add_movie()
                except IndexError:
                    break
