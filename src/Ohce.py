class Ohce:
    def __init__(self, language, translation, day_period):
        self.language = language
        self.translation = translation
        self.day_period = day_period

    def hello(self):
        return self.translation[self.language][self.day_period]["HELLO"] + "\n"

    def goodbye(self):
        return self.translation[self.language][self.day_period]["GOODBYE"]

    def bien_dit(self):
        return self.translation[self.language]["WELL_SAID"] + "\n"

    def reversed(self, world):
        return world[::-1] + "\n"

    def palindrome(self, world):
        bien_dit = self.bien_dit() if self.reversed(world) == world + "\n" else ""

        return self.hello() + self.reversed(world) + bien_dit + self.goodbye()
