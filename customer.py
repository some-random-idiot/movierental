from rental import Rental, PriceCode
from movie import Movie


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        return self.name

    def compute_rental_points(self):
        frequent_renter_points = 0
        for rental in self.rentals:
            frequent_renter_points += rental.get_freq_rental_point()
        return frequent_renter_points

    def compute_total_charge(self):
        total_amount = 0
        for rental in self.rentals:
            total_amount += rental.get_charge()
        return total_amount

    def statement(self):
        """
            Print all the rentals in current period, 
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        total_amount = self.compute_total_charge()  # total charges
        frequent_renter_points = self.compute_rental_points()
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            statement += fmt.format(rental.movie.get_title(), rental.days_rented, rental.get_charge())

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
            "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon")
    customer.add_rental(Rental(movie, 2, PriceCode.regular))
    movie = Movie("CitizenFour")
    customer.add_rental(Rental(movie, 3, PriceCode.new_release))
    print(customer.statement())
