import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.bar import Bar

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song('Bruce Springsteen', 'Dancing in the Dark', 239)
    
    def test_has_artist(self):
        self.assertEqual('Bruce Springsteen', self.song.artist)

    def test_has_title(self):
        self.assertEqual('Dancing in the Dark', self.song.title)

    def test_has_minutes(self):
        self.assertEqual(239, self.song.minutes)