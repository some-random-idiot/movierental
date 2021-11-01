import csv


class MovieCatalog:
    """A movie catalog. It contains various movies."""
    def __init__(self):
        self.catalog = {}
        self.last_index = 0

    def add_movie(self):
        with open('movies.csv', 'r') as f:
            rows = list(csv.reader(f))
            self.catalog[rows[self.last_index][1]] = Movie(rows[self.last_index][1], rows[self.last_index][2],
                                                     rows[self.last_index][3].split(sep='|'))
        self.last_index += 1

    def get_movie(self, title):
        while True:
            if title in self.catalog:
                return self.catalog[title]
            else:
                try:
                    self.add_movie()
                except IndexError:
                    break


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
