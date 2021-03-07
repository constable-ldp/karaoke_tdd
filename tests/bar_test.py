import unittest
from classes.guest import Guest
from classes.bar import Bar
from classes.drinks import Drinks

class TestBar(unittest.TestCase):
    def setUp(self):
        self.guest = Guest('John', 18, 100.00, 4, 0, 'Bruce Springsteen', 
                            'Dancing in the Dark', None, False)
        self.bar = Bar(1000, [])
        self.drinks = Drinks('Ale', 4.99, 2)

    def test_has_till(self):
        self.assertEqual(1000, self.bar.till)

    def test_has_drinks(self):
        self.assertEqual([], self.bar.drinks)

    def test_add_new_drink(self):
        self.bar.add_new_drink(self.drinks)
        self.assertEqual('Ale', self.bar.drinks[0].name)

    def test_check_underage__pass(self):
        self.assertEqual(False, self.bar.check_underage(self.guest))

    def test_check_underage__fail(self):
        new_guest = Guest('John', 17, 100.00, 4, 0, 'Bruce Springsteen', 
                            'Dancing in the Dark', None, False)
        self.assertEqual(True, self.bar.check_underage(new_guest))

    def test_check_find_drink_by_name(self):
        self.bar.add_new_drink(self.drinks)
        new_drinks = self.bar.find_drink_by_name('Ale')
        self.assertEqual('Ale', new_drinks.name)

    def test_check_buy_drinks(self):
        self.bar.add_new_drink(self.drinks)
        self.bar.buy_drinks('Ale', self.bar, self.guest)
        self.assertEqual(2, self.guest.drunkeness)
        self.assertEqual(95.01, self.guest.wallet)