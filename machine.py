import reflector


class Machine:
    def __init__(self):
        self.rotorList = []
        self.reflector = reflector.Reflector()
        self.carry = None
        self.status = [0, 0]
        self.rotor_length = 0

    def add_rotor(self, rotor_):
        self.rotorList.append(rotor_)
        if not self.rotor_length:
            self.rotor_length = len(rotor_.in_set)

    def change_reflector(self, reflector_):
        self.reflector = reflector_

    def encode(self, letter):
        self.carry = letter

        for r in self.rotorList:
            self.carry = r.encode(self.carry)

        self.carry = self.reflector.encode(self.carry)

        for r in reversed(self.rotorList):
            self.carry = r.decode(self.carry)

        self.rotate()
        return self.carry

    def rotate(self):
        self.status[1] += 1
        self.rotorList[self.status[0]].rotate(self.status[1])
        if self.status[1] >= 26:
            self.status[0] = (self.status[0] + 1) % len(self.rotorList)
            self.status[1] = 0
