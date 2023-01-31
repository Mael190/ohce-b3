import locale
import unittest
import datetime
from src.Languages.Constants import Translation
from src.utilities.OhceBuilder import OhceBuilder
from src import Period


class DefaultTest(unittest.TestCase):

    def test_default(self):
        system_language = locale.getdefaultlocale()[0]
        period = Period.get_day_period(datetime.datetime.now().hour)
        ohce_builder = OhceBuilder()
        ohce_builder.set_day_period(period)
        ohce_builder.set_language(system_language)
        ohce = ohce_builder.build()

        # QUAND on saisit une chaîne
        world = input('Saissiez un mot\n')
        result = ohce.palindrome(world).split("\n")

        # ALORS dans la langue bonjour, puis la chaine en miroir puis au revoir sont revnoyées
        self.assertEqual(Translation[system_language][period]["HELLO"], result[0])
        self.assertEqual(world[::-1], result[1])
        self.assertEqual(Translation[system_language][period]["GOODBYE"], result[-1])
