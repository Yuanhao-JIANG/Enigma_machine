class Rotor:
    def __init__(self, out_set=None):
        self.in_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
        if out_set:
            self.out_set = out_set
        else:
            self.out_set = self.in_set
        self.map = {}
        self.rotate(0)

    def encode(self, letter):
        return self.map[letter]

    def decode(self, letter):
        return list(self.map.keys())[list(self.map.values()).index(letter)]

    def rotate(self, n):
        for i in range(len(self.in_set)):
            self.map[self.in_set[i]] = self.out_set[(i+n) % len(self.in_set)]
