import unittest

class TestAssertions(unittest.TestCase):

    def test_basic_assertions(self):
        self.assertEqual(10, 10)          # Pass
        self.assertNotEqual(10, 5)
        self.assertTrue(5 > 1)
        self.assertFalse(5 < 1)
