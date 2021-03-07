import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('John', 18, 100.00, 4, 0, 'Bruce Springsteen', 
                            'Dancing in the Dark', None, False)
        self.song = Song('Bruce Springsteen', 'Dancing in the Dark', 239)
        self.room = Room(1, 14.99, [self.song], 4, 8)
    
    def test_has_name(self):
        self.assertEqual('John', self.guest.name)
        
    def test_has_age(self):
        self.assertEqual(18, self.guest.age)

    def test_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_has_fun(self):
        self.assertEqual(4, self.guest.fun)
    
    def test_has_drunkeness(self):
        self.assertEqual(0, self.guest.drunkeness)
    
    def test_has_favourite_artist(self):
        self.assertEqual('Bruce Springsteen', self.guest.favourite_artist)

    def test_has_favourite_song(self):
        self.assertEqual('Dancing in the Dark', self.guest.favourite_song)

    def test_has_room_number(self):
        self.assertEqual(None, self.guest.room_number)

    def test_has_checked_in(self):
        self.assertEqual(False, self.guest.checked_in)

    def test_find_favourite_song__pass(self):
        self.assertEqual('Wooo! This is my favourite song!', self.guest.find_favourite_song(self.room, self.song))
        self.assertEqual(6, self.guest.fun)

    def test_find_favourite_song__fail(self):
        guest = Guest('John', 18, 100.00, 4, 0, 'Bruce Springsteen', 
                    'The River', None, False)
        self.assertEqual(None, guest.find_favourite_song(self.room, self.song))
        self.assertEqual(4, guest.fun)

    def test_find_favourite_song__fail2(self):
        guest = Guest('John', 18, 100.00, 10, 0, 'Bruce Springsteen', 
                    'Dancing in the Dark', None, False)
        self.assertEqual('Wooo! This is my favourite song!', guest.find_favourite_song(self.room, self.song))
        self.assertEqual(10, guest.fun)
    
    def test_find_favourite_artist__pass(self):
        self.assertEqual('Nice, I love this band!', self.guest.find_favourite_artist(self.room, self.song))
        self.assertEqual(5, self.guest.fun)

    def test_find_favourite_artist__fail(self):
        guest = Guest('John', 18, 100.00, 4, 0, 'Future Islands', 
                    'Dancing in the Dark', None, False)
        self.assertEqual(None, guest.find_favourite_artist(self.room, self.song))
        self.assertEqual(4, guest.fun)

    def test_find_favourite_artist__fail2(self):
        guest = Guest('John', 18, 100.00, 10, 0, 'Bruce Springsteen', 
                    'Dancing in the Dark', None, False)
        self.assertEqual('Nice, I love this band!', guest.find_favourite_artist(self.room, self.song))
        self.assertEqual(10, guest.fun)