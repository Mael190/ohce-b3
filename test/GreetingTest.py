import unittest
from src.Ohce import Ohce

class GreetingTest(unittest.TestCase):
    def test_hello(self):
        ohce = Ohce
        resultat = ohce.palindrome("kiwi").split("\n")

        self.assertEqual("Bonjour", resultat[0])
    
    def test_goodbye(self):
        ohce = Ohce
        resultat = ohce.palindrome("kiwi").split("\n")

        self.assertEqual("Au revoir", resultat[3])

if __name__ == '__main__':
    unittest.main()



