import unittest
from shuffle import helper


class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        self.assertEqual(helper(), ":)")
