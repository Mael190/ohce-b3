import unittest
import parameterized as parameterized
from src.Ohce import Ohce
from src.Languages.Constants import Translation
from unittest.mock import Mock
from src.utilities.OhceBuilder import OhceBuilder


class PalindromeTest(unittest.TestCase):

    @parameterized.parameterized.expand([
        "fr_FR",
        "en_EN",
    ])
    def test_reversed(self, language):
        world = "kiwi"

        # QUAND on saisit une chaîne
        ohce = OhceBuilder.default()
        ohce.hello = ohce.goodbye = Mock()
        ohce.hello.return_value = ohce.goodbye.return_value = ""
        result = ohce.reversed(world)

        # ALORS celle-ci est renvoyée en miroir sans prendre en compte la langue
        self.assertIn(world[::-1], result)

    @parameterized.parameterized.expand([
        ["fr_FR", Translation["fr_FR"]["WELL_SAID"]],
        ["en_EN", Translation["en_EN"]["WELL_SAID"]],
    ])
    def test_palindrome(self, language, well_said):
        world = "kayak"

        # QUAND on saisit un palindrome
        ohce_builder = OhceBuilder()
        ohce_builder.set_language(language)
        ohce = ohce_builder.build()
        ohce.hello = ohce.goodbye = Mock()
        ohce.hello.return_value = ohce.goodbye.return_value = ""
        result = ohce.palindrome(world).split("\n")

        # ALORS celui-ci est renvoyé ET « Bien dit » de la langue est envoyé ensuite
        self.assertEqual(world, result[0])
        self.assertEqual(well_said, result[1])

    def test_nonpalindrome(self):
        world = "kiwi"

        # QUAND on saisit un palindrome
        ohce = OhceBuilder.default()
        ohce.hello = ohce.goodbye = Mock()
        ohce.hello.return_value = ohce.goodbye.return_value = ""
        result = ohce.palindrome(world)

        # ALORS celui-ci est renvoyé
        self.assertEqual(world[::-1] + '\n', result)
