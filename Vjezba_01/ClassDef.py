import random
import math


class Boson:
    isFermion = False

    def __init__(self, name, spin, momentum):
        self.name = name
        self.spin = spin
        self.momentum = momentum

    def PrintInfo(self):
        print("Ime:", self.name)
        print("Spin:", self.spin)
        print("Impuls:", self.momentum)
        print("Je li fermion:", self.isFermion)


class Higgs(Boson):
    MassSigma = 1

    def __init__(self, name, spin, momentum, MassMean):
        super().__init__(name, spin, momentum)
        self.MassMean = MassMean

    def Energy(self):
        masa = random.gauss(self.MassMean, self.MassSigma)
        energija = math.sqrt(masa**2 + self.momentum**2)
        return energija