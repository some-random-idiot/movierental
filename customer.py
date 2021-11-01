from rental import Rental
from movie import Movie
from datetime import datetime


class Customer:
    """A customer who rents movies.
    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental record to the customer's list of rental records."""
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self) -> str:
        """Get the name of the customer"""
        return self.name

    def compute_rental_points(self) -> int:
        """Compute the total rental point(s) gained from rentals belonging to this customer."""
        frequent_renter_points = 0
        for rental in self.rentals:
            frequent_renter_points += rental.get_freq_rental_point()
        return frequent_renter_points

    def compute_total_charge(self) -> float:
        """Computes the total charge accumulated through rentals."""
        total_amount = 0
        for rental in self.rentals:
            total_amount += rental.get_charge()
        return total_amount

    def statement(self) -> str:
        """Print all the rentals in current period,
        along with total charges and reward points.

        Returns:
            The statement as a String
        """
        total_amount = self.compute_total_charge()
        frequent_renter_points = self.compute_rental_points()
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            statement += fmt.format(rental.movie.get_title(), rental.days_rented, rental.get_charge())

        # Footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
            "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", "2001", ["Horror", "Sci-Fi"])
    customer.add_rental(Rental(movie, 2))
    movie = Movie("An Unnamed Current Year Film", str(datetime.now().year), ["Action", "Adventure"])
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
