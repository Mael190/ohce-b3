from src.Ohce import Ohce
from src.Languages.Constants import Translation


class OhceBuilder():
    def __init__(self):
        self.language = "fr_FR"
        self.translation = Translation
        self.day_period = "MORNING"

    def build(self):
        return Ohce(self.language, self.translation, self.day_period)

    @staticmethod
    def default():
        return OhceBuilder().build()

    def set_language(self, language):
        self.language = language

    def set_day_period(self, day_period):
        self.day_period = day_period
