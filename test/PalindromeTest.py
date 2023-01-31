import unittest
import parameterized as parameterized
from src.Ohce import Ohce
from src.Languages.Constants import Translation
from unittest.mock import Mock


class PalindromeTest(unittest.TestCase):

    @parameterized.parameterized.expand([
        "fr_FR",
        "en_EN",
    ])
    def test_reversed(self, language):
        world = "kiwi"

        # QUAND on saisit une chaîne
        ohce = Ohce(language, Translation)
        ohce.hello = ohce.goodbye = Mock()
        ohce.hello.return_value = ohce.goodbye.return_value = ""
        result = ohce.reversed(world)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(world[::-1], result)

    @parameterized.parameterized.expand([
        ["fr_FR", Translation["fr_FR"]["WELL_SAID"]],
        ["en_EN", Translation["en_EN"]["WELL_SAID"]],
    ])
    def test_palindrome(self, language, well_said):
        world = "kayak"

        # QUAND on saisit un palindrome
        ohce = Ohce(language, Translation)
        ohce.hello = ohce.goodbye = Mock()
        ohce.hello.return_value = ohce.goodbye.return_value = ""
        result = ohce.palindrome(world).split("\n")

        # ALORS celui-ci est renvoyé ET « Bien dit » est envoyé ensuite
        self.assertEqual(world, result[0])
        self.assertEqual(well_said, result[1])
