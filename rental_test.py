import unittest
from rental import Rental
from movie import Movie
from datetime import datetime


class RentalTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("An Unnamed Current Year Film", str(datetime.now().year), ["Action", "Adventure"])
        self.regular_movie = Movie("CitizenFour", "2014", ["Documentary"])
        self.childrens_movie = Movie("Frozen", "2013", ["Adventure", "Fantasy", "Children"])

        self.test_rental_price_cases = [(self.new_movie, 1, 3.0),
                                        (self.new_movie, 5, 15.0),
                                        (self.regular_movie, 2, 2.0),
                                        (self.regular_movie, 10, 14.0),
                                        (self.childrens_movie, 3, 1.5),
                                        (self.childrens_movie, 7, 7.5)]
        self.test_rental_points_cases = [(self.new_movie, 5, 5),
                                         (self.new_movie, 10, 10),
                                         (self.regular_movie, 5, 1),
                                         (self.regular_movie, 10, 1),
                                         (self.childrens_movie, 5, 1),
                                         (self.childrens_movie, 10, 1)]

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Shrek", "2001", ["Comedy", "Fantasy"])
        self.assertEqual("Shrek", m.get_title())

    def test_rental_price(self):
        for movie_type, days, charge in self.test_rental_price_cases:
            with self.subTest():
                rental = Rental(movie_type, days)
                self.assertEqual(rental.get_charge(), charge)

    def test_rental_points(self):
        for movie_type, days, points in self.test_rental_points_cases:
            with self.subTest():
                rental = Rental(movie_type, days)
                self.assertEqual(rental.get_freq_rental_point(), points)
