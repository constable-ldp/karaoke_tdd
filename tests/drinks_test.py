import unittest
from classes.drinks import Drinks

class TestDrinks(unittest.TestCase):
    
    def setUp(self):
        self.drinks = Drinks('Ale', 4.99, 3)

    def test_has_name(self):
        self.assertEqual('Ale', self.drinks.name)

    def test_has_price(self):
        self.assertEqual(4.99, self.drinks.price)

    def test_has_alcohol_level(self):
        self.assertEqual(3, self.drinks.alcohol_level)