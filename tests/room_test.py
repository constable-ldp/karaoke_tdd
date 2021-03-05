import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 14.99, 4, 8, False)
    
    def test_has_room_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_has_price(self):
        self.assertEqual(14.99, self.room.price)

    def test_has_max_capacity(self):
        self.assertEqual(4, self.room.current_capacity)

    def test_has_current_capacity(self):
        self.assertEqual(8, self.room.max_capacity)
    
    def test_is_premium(self):
        self.assertEqual(False, self.room.premium)