import unittest
from unittest.mock import Mock
import parameterized
from src.Languages.Constants import Translation
from src.utilities.OhceBuilder import OhceBuilder


class GreetingTest(unittest.TestCase):
    @parameterized.parameterized.expand([
        ["fr_FR", "MORNING"],
        ["fr_FR", "AFTERNOON"],
        ["fr_FR", "EVENING"],
        ["fr_FR", "NIGHT"],
        ["en_EN", "MORNING"],
        ["en_EN", "AFTERNOON"],
        ["en_EN", "EVENING"],
        ["en_EN", "NIGHT"],
    ])
    def test_hello(self, language, period):
        ohce_builder = OhceBuilder()
        ohce_builder.set_day_period(period)
        ohce_builder.set_language(language)
        ohce = ohce_builder.build()
        ohce.reversed = ohce.goodbye = Mock()
        ohce.reversed.return_value = ohce.goodbye.return_value = ""

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("kiwi")

        # ALORS «Bonjour» de la langue et en fonction de la période est envoyé avant toute réponse
        self.assertIn(Translation[language][period]["HELLO"], resultat)

    @parameterized.parameterized.expand([
        ["fr_FR", "MORNING"],
        ["fr_FR", "AFTERNOON"],
        ["fr_FR", "EVENING"],
        ["fr_FR", "NIGHT"],
        ["en_EN", "MORNING"],
        ["en_EN", "AFTERNOON"],
        ["en_EN", "EVENING"],
        ["en_EN", "NIGHT"],
    ])
    def test_goodbye(self, language, period):
        ohce_builder = OhceBuilder()
        ohce_builder.set_day_period(period)
        ohce_builder.set_language(language)
        ohce = ohce_builder.build()
        ohce.reversed = ohce.hello = Mock()
        ohce.reversed.return_value = ohce.hello.return_value = ""

        # QUAND on saisit une chaîne
        resultat = ohce.palindrome("kiwi")

        #  ALORS «Au revoir» de la langue et en fonction de la période est envoyé en dernier
        self.assertIn(Translation[language][period]["GOODBYE"], resultat)


if __name__ == '__main__':
    unittest.main()
