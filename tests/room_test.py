import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.bar import Bar

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest = Guest('John', 18, 100.00, 4, 0, False, 'Bruce Springsteen', 
                            'Dancing in the Dark', None, False, 180)
        self.song = Song('Bruce Springsteen', 'Dancing in the Dark', 239)
        self.room = Room(1, 14.99, [], 4, 8, False)
    
    def test_has_room_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_has_price(self):
        self.assertEqual(14.99, self.room.price)

    def test_has_max_capacity(self):
        self.assertEqual(4, self.room.current_capacity)

    def test_has_current_capacity(self):
        self.assertEqual(8, self.room.max_capacity)
    
    def test_has_premium(self):
        self.assertEqual(False, self.room.premium)

    def test_check_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(5, self.room.current_capacity)
        self.assertEqual(85.01, self.guest.wallet)
        self.assertEqual(1, self.guest.room_number)
        self.assertEqual(True, self.guest.checked_in)

    def test_check_in__fail_capacity(self):
        new_room = Room(1, 14.99, [], 8, 8, False)
        new_room.check_in(self.guest)
        self.assertEqual(8, new_room.current_capacity)

    def test_check_in__fail_money(self):
        new_guest = Guest('John', 18, 10.00, 4, 0, False, 'Bruce Springsteen', 
                        'Dancing in the Dark', None, False, 180)
        self.room.check_in(new_guest)
        self.assertEqual(4, self.room.current_capacity)

    def test_check_in__fail_checked_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(5, self.room.current_capacity)
        self.room.check_in(self.guest)
        self.assertEqual(5, self.room.current_capacity)

    def test_check_out(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(4, self.room.current_capacity)

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual('Bruce Springsteen', self.room.songs[0].artist)
