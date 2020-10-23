class Modulo:
    def __init__(self, mod, value):
        self.mod = mod
        self.value = value % mod

    def __repr__(self):
        return str(self.value) + " (mod " + str(self.mod) + ")"

    def __add__(self, other):   # other needs (!) to be of same modulo
        return Modulo(self.mod, (self.value + other.value) % self.mod)

    def __eq__(self, other):    # other needs (!) to be of same modulo
        if self.value == other.value:
            return True
        else: return False

    def add(self, n):
        self.value = (self.value+n) % self.mod
        return self
