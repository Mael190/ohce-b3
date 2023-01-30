from src.Ohce import Ohce
from src.Languages.Constants import Translation

if __name__ == '__main__':
    ohce = Ohce("fr_FR", Translation)
    print(ohce.hello())