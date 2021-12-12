class Reflector:
    def __init__(self, map1=None):
        if map1 is None:
            map1 = {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j', 'k': 'l', 'm': 'n', 'o': 'p', 'q': 'r',
                    's': 't', 'u': 'v', 'w': 'x', 'y': 'z'}
        for letter in list(map1.values()):
            map1[letter] = list(map1.keys())[list(map1.values()).index(letter)]

        self.map = map1

    def encode(self, letter):
        return self.map[letter]
