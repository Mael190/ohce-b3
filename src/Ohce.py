class Ohce:
    def hello(self):
        return "Bonjour"

    def goodbye(self):
        return "Au revoir"
        
    def palindrome(self, world):
        reversed = world[::-1]
        bienDit = "Bien dit\n" if reversed == world else ""

        return self.hello()+ "\n" + reversed + "\n" + bienDit + self.goodbye()