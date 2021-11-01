import unittest
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("Mulan", "2010", ["Action", "Adventure"])
        self.regular_movie = Movie("CitizenFour", "2004", ["Documentary"])
        self.childrens_movie = Movie("Frozen", "2012", ["Adventure", "Fantasy"])

        self.test_rental_price_cases = [(self.new_movie, 1, 3.0, PriceCode.new_release),
                                        (self.new_movie, 5, 15.0, PriceCode.new_release),
                                        (self.regular_movie, 2, 2.0, PriceCode.regular),
                                        (self.regular_movie, 10, 14.0, PriceCode.regular),
                                        (self.childrens_movie, 3, 1.5, PriceCode.childrens),
                                        (self.childrens_movie, 7, 7.5, PriceCode.childrens)]
        self.test_rental_points_cases = [(self.new_movie, 5, 5, PriceCode.new_release),
                                         (self.new_movie, 10, 10, PriceCode.new_release),
                                         (self.regular_movie, 5, 1, PriceCode.regular),
                                         (self.regular_movie, 10, 1, PriceCode.regular),
                                         (self.childrens_movie, 5, 1, PriceCode.childrens),
                                         (self.childrens_movie, 10, 1, PriceCode.childrens)]

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", "2004", ["Documentary"])
        self.assertEqual("CitizenFour", m.get_title())

    def test_rental_price(self):
        for movie_type, days, charge, price_code in self.test_rental_price_cases:
            with self.subTest():
                rental = Rental(movie_type, days)
                self.assertEqual(rental.get_charge(), charge)

    def test_rental_points(self):
        for movie_type, days, points, price_code in self.test_rental_points_cases:
            with self.subTest():
                rental = Rental(movie_type, days)
                self.assertEqual(rental.get_freq_rental_point(), points)
