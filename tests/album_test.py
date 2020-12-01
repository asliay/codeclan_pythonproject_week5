import unittest

from models.album import Album
from models.artist import Artist
from models.label import Label

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Frightened Rabbit")

        self.label = Label("Fat Cat Records")

        self.album = Album("Midnight Organ Fight", self.artist, "Indie Rock", 22.99, 13.79, "2008", "https://is2-ssl.mzstatic.com/image/thumb/Music123/v4/53/79/37/53793762-eeef-8cce-96b2-6de1c18740e2/source/600x600bb.jpg", 6, self.label)

    def test_album_has_title(self):
        self.assertEqual("Midnight Organ Fight", self.album.title)

    def test_album_has_artist(self):
        self.assertEqual(self.artist, self.album.artist)

    def test_album_has_genre(self):
        self.assertEqual("Indie Rock", self.album.genre)

    def test_album_has_price(self):
        self.assertEqual(22.99, self.album.price)
    
    def test_album_has_cost_price(self):
        self.assertEqual(13.79, self.album.cost_price)

    def test_album_has_release_year(self):
        self.assertEqual("2008", self.album.release_year)

    def test_album_has_cover_art(self):
        self.assertEqual("https://is2-ssl.mzstatic.com/image/thumb/Music123/v4/53/79/37/53793762-eeef-8cce-96b2-6de1c18740e2/source/600x600bb.jpg", self.album.cover_art)

    def test_album_has_stock(self):
        self.assertEqual(6, self.album.stock)

    def test_album_has_label(self):
        self.assertEqual(self.label, self.album.label)