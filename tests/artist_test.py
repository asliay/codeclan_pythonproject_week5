import unittest

from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Frightened Rabbit")

    def test_artist_has_name(self):
        self.assertEqual("Frightened Rabbit", self.artist.name)