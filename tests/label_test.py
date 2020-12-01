import unittest

from models.label import Label

class TestLabel(unittest.TestCase):
    def setUp(self):
        self.label = Label("Atlantic Records")

    def test_label_has_name(self):
        self.assertEqual("Atlantic Records", self.label.name)