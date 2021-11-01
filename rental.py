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

    def get_title(self):
        return self.movie.title

    def get_charge(self):
        # compute rental change
        return self.movie.get_price_code().price(self.days_rented)

    def get_freq_rental_point(self):
        # award renter points
        frequent_renter_points = self.movie.get_price_code().frequent_renter_point(self.days_rented)
        return frequent_renter_points
