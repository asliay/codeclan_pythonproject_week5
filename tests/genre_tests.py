import unittest

from models.genre import Genre

class TestGenre(unittest.TestCase):
    def setUp(self):
        self.genre = Genre("Indie Rock")

    def test_genre_has_category(self):
        self.assertEqual("Indie Rock", self.genre.category)
