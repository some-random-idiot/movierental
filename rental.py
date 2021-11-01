from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    regular = {"price": lambda days: 2.0 + 1.5 * (days - 2),
               "frp": lambda days: 1
               }
    childrens = {"price": lambda days: 1.5 + 1.5 * (days - 3),
                 "frp": lambda days: 1
                 }

    def price(self, days):
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def frequent_renter_point(self, days):
        frp = self.value["frp"]
        return frp(days)


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

    def __init__(self, movie, days_rented, price_code):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_title(self):
        return self.movie.title

    def get_charge(self):
        # compute rental change
        return self.price_code.price(self.days_rented)

    def get_freq_rental_point(self):
        # award renter points
        frequent_renter_points = self.price_code.frequent_renter_point(self.days_rented)
        return frequent_renter_points
