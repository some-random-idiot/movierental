import logging

from ISPCodes.movierental.movie import Movie


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

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_charge(self, rental):
        # compute rental change
        amount = 0
        if rental.get_movie().get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 each.
            amount = 2.0
            if rental.get_days_rented() > 2:
                amount += 1.5 * (rental.get_days_rented() - 2)
        elif rental.get_movie().get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 each.
            amount = 1.5
            if rental.get_days_rented() > 3:
                amount += 1.5 * (rental.get_days_rented() - 3)
        elif rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
            # Straight per day charge
            amount = 3 * rental.get_days_rented()
        else:
            log = logging.getLogger()
            log.error(f"Movie {rental.get_movie()} has unrecognized priceCode {rental.get_movie().get_price_code()}")
        return amount

    def get_freq_rental_point(self, frequent_renter_points, rental):
        # award renter points
        if rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
            frequent_renter_points += rental.get_days_rented()
        else:
            frequent_renter_points += 1
        return frequent_renter_points
