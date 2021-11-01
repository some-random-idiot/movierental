from movie import Movie
from enum import Enum
from datetime import datetime


class PriceCode(Enum):
    """An enumeration for different kinds of movies' price codes."""

    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    regular = {"price": lambda days: 2.0 + 1.5 * (days - 2),
               "frp": lambda days: 1
               }
    childrens = {"price": lambda days: 1.5 + 1.5 * (days - 3),
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        """Return the rental price according to the given number of day(s)"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def frequent_renter_point(self, days: int) -> int:
        """Return the frequent renter point according to the given number of day(s)"""
        frp = self.value["frp"]
        return frp(days)

    @classmethod
    def for_movie(cls, movie: Movie) -> Enum:
        """Determine the price code of a movie."""
        if movie.get_year() == str(datetime.now().year):
            return cls.new_release
        elif "Children" in movie.get_genre_list():
            return cls.childrens
        else:
            return cls.regular


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie: Movie, days_rented: int):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = PriceCode.for_movie(movie)

    def get_title(self) -> str:
        """Get the title of the rented movie."""
        return self.movie.get_title()

    def get_charge(self) -> float:
        """Get the rental charge according to the price code."""
        return self.price_code.price(self.days_rented)

    def get_freq_rental_point(self) -> int:
        """Get the frequent renter point(s) accumulated from this rental."""
        frequent_renter_points = self.price_code.frequent_renter_point(self.days_rented)
        return frequent_renter_points
