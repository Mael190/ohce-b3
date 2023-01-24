import unittest
from src import Ohce

class PalindromeTest(unittest.TestCase):
    def test_reversed(self):
        world = "kiwi"

        ohce = Ohce()
        result = ohce.palindrome(world).split("\n")

        self.assertEqual(world[::-1], result[1])
    
    def test_palindrome(self):
        world = "kayac"

        ohce = Ohce()
        result = ohce.palindrome(world).split("\n")

        self.assertEqual(world, result[1])
        self.assertEqual("Bien dit", result[2])
    


