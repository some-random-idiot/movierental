import unittest
from rental import Rental
from movie import *


class RentalTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("Mulan", PriceCode.new_release)
        self.regular_movie = Movie("CitizenFour", PriceCode.regular)
        self.childrens_movie = Movie("Frozen", PriceCode.childrens)

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
        m = Movie("CitizenFour", PriceCode.regular)
        self.assertEqual("CitizenFour", m.get_title())
        self.assertEqual(PriceCode.regular, m.get_price_code())

    def test_rental_price(self):
        for movie_type, days, charge in self.test_rental_price_cases:
            with self.subTest():
                rental = Rental(movie_type, days)
                self.assertEqual(rental.get_charge(), charge)

    def test_rental_points(self):
        for movie_type, days, points in self.test_rental_points_cases:
            with self.subTest():
                rental = Rental(movie_type, days)
                self.assertEqual(rental.get_freq_rental_point(0), points)
