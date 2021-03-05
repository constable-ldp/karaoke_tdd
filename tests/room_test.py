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
    
    def test_has_premium(self):
        self.assertEqual(False, self.room.premium)

    def test_check_in(self):
        self.assertEqual(5, self.room.current_capacity)

    def test_check_in__above_max(self):
        new_room = Room(1, 14.99, 8, 8, False)
        
        self.assertEqual(8, new_room.current_capacity)

    def test_check_in__in_other_room(self):
        pass
        #self.assertEqual('Customer needs to check out before moving to new room',)

    def test_check_in__money_available(self):
        pass

    def test_check_out(self):
        pass
