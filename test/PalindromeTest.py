import unittest
import parameterized as parameterized
from src.Ohce import Ohce
from src.Languages.Constants import Translation


class PalindromeTest(unittest.TestCase):

    @parameterized.parameterized.expand([
        "fr_FR",
        "en_EN",
    ])
    def test_reversed(self, language):
        world = "kiwi"

        # QUAND on saisit une chaîne
        ohce = Ohce(language, Translation)
        result = ohce.palindrome(world).split("\n")

        # ALORS celle-ci est renvoyée en miroir
        self.assertEqual(world[::-1], result[1])

    @parameterized.parameterized.expand([
        ["fr_FR", Translation["fr_FR"]["WELL_SAID"]],
        ["en_EN", Translation["en_EN"]["WELL_SAID"]],
    ])
    def test_palindrome(self, language, well_said):
        world = "kayak"

        # QUAND on saisit un palindrome
        ohce = Ohce(language, Translation)
        result = ohce.palindrome(world).split("\n")

        # ALORS celui-ci est renvoyé ET « Bien dit » est envoyé ensuite
        self.assertEqual(world, result[1])
        self.assertEqual(well_said, result[2])
