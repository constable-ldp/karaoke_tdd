import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest('John', 18, 100.00, 4, 0, 'Bruce Springsteen', 'Dancing in the Dark')
    
    def test_has_name(self):
        self.assertEqual('John', self.guest.name)
        
    def test_has_age(self):
        self.assertEqual(18, self.guest.age)

    def test_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_has_rowdiness(self):
        self.assertEqual(4, self.guest.rowdiness)
    
    def test_has_drunkeness(self):
        self.assertEqual(0, self.guest.drunkeness)
    
    def test_has_favourite_artist(self):
        self.assertEqual('Bruce Springsteen', self.guest.favourite_artist)

    def test_has_favourite_song(self):
        self.assertEqual('Dancing in the Dark', self.guest.favourite_song)