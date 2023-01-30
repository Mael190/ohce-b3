import unittest
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

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("kiwi").split("\n")

        # ALORS «Bonjour» est envoyé avant toute réponse
        self.assertEqual(hello, resultat[0])

    @parameterized.parameterized.expand([
        ["fr_FR", Translation["fr_FR"]["GOODBYE"]],
        ["en_EN", Translation["en_EN"]["GOODBYE"]],
    ])
    def test_goodbye(self, language, goodbye):
        ohce = Ohce(language, Translation)

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("kiwi").split("\n")

        #  ALORS «Au revoir»  est envoyé en dernier
        self.assertEqual(goodbye, resultat[2])


if __name__ == '__main__':
    unittest.main()
