# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from datetime import datetime


def make_movies():
    movies = [
        Movie("An Unnamed Current Year Film 1", str(datetime.now().year), ["Horror", "Comedy"]),
        Movie("CitizenFour", "2014", ["Documentary"]),
        Movie("Frozen", "2013", ["Adventure", "Fantasy", "Children"]),
        Movie("An Unnamed Current Year Film 2", str(datetime.now().year), ["Action", "Adventure"]),
        Movie("Particle Fever", "2013", ["Documentary", "Sci-Fi"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
