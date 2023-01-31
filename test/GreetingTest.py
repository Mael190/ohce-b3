import unittest
from unittest.mock import Mock
import parameterized
from src.Ohce import Ohce
from src.Languages.Constants import Translation


class GreetingTest(unittest.TestCase):
    @parameterized.parameterized.expand([
        ["fr_FR", Translation["fr_FR"]["HELLO"]],
        ["en_EN", Translation["en_EN"]["HELLO"]],
    ])
    def test_hello(self, language, hello):
        ohce = Ohce(language, Translation)
        ohce.reversed = ohce.goodbye = Mock()
        ohce.reversed.return_value = ohce.goodbye.return_value = ""

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("kiwi")

        # ALORS «Bonjour» est envoyé avant toute réponse
        self.assertIn(hello, resultat)

    @parameterized.parameterized.expand([
        ["fr_FR", Translation["fr_FR"]["GOODBYE"]],
        ["en_EN", Translation["en_EN"]["GOODBYE"]],
    ])
    def test_goodbye(self, language, goodbye):
        ohce = Ohce(language, Translation)
        ohce.reversed = ohce.hello = Mock()
        ohce.reversed.return_value = ohce.hello.return_value = ""

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("kiwi")

        #  ALORS «Au revoir»  est envoyé en dernier
        self.assertIn(goodbye, resultat)


if __name__ == '__main__':
    unittest.main()
