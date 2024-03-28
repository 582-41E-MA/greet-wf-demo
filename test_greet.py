import unittest
import greet

class TestAdd(unittest.TestCase):
    def test_int(self):
        self.assertEqual(greet.add(1, 2), 3)