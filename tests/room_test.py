import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest('John', 18, 100.00, 4, 0, 'Bruce Springsteen', 
                            'Dancing in the Dark', None, False)
        self.song = Song('Bruce Springsteen', 'Dancing in the Dark', 239)
        self.room = Room(1, 14.99, [], 4, 8)
    
    def test_has_room_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_has_price(self):
        self.assertEqual(14.99, self.room.price)

    def test_has_max_capacity(self):
        self.assertEqual(4, self.room.current_capacity)

    def test_has_current_capacity(self):
        self.assertEqual(8, self.room.max_capacity)

    def test_check_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(5, self.room.current_capacity)
        self.assertEqual(85.01, self.guest.wallet)
        self.assertEqual(1, self.guest.room_number)
        self.assertEqual(True, self.guest.checked_in)

    def test_check_in__fail_capacity(self):
        new_room = Room(1, 14.99, [], 8, 8)
        new_room.check_in(self.guest)
        self.assertEqual(8, new_room.current_capacity)

    def test_check_in__fail_money(self):
        new_guest = Guest('John', 18, 10.00, 4, 0, 'Bruce Springsteen', 
                        'Dancing in the Dark', None, False)
        self.room.check_in(new_guest)
        self.assertEqual(4, self.room.current_capacity)

    def test_check_in__fail_checked_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(5, self.room.current_capacity)
        self.room.check_in(self.guest)
        self.assertEqual(5, self.room.current_capacity)

    def test_check_out__pass(self):
        self.room.checked_in = True
        self.room.check_out(self.guest)
        self.assertEqual(4, self.room.current_capacity)

    def test_check_out__fail(self):
        self.room.check_out(self.guest)
        self.assertEqual(4, self.room.current_capacity)

    def test_add_song__pass(self):
        self.room.add_song(self.song)
        self.assertEqual('Bruce Springsteen', self.room.songs[0].artist)

    def test_add_song__cant_add_same_song(self):
        self.room.add_song(self.song)
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))
