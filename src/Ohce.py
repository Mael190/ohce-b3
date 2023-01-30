class Ohce:
    def __init__(self, language, translation):
        self.language = language
        self.translation = translation

    def hello(self):
        return self.translation[self.language]["HELLO"]

    def goodbye(self):
        return self.translation[self.language]["GOODBYE"]

    def bien_dit(self):
        return self.translation[self.language]["WELL_SAID"]

    def palindrome(self, world):
        reversed = world[::-1]
        bien_dit = self.bien_dit() + "\n" if reversed == world else ""

        return self.hello() + "\n" + reversed + "\n" + bien_dit + self.goodbye()
