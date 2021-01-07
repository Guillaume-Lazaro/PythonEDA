from Courrier import *

class Colis(Courrier):

    def __init__(self, adrDest, adrExp, poids, expMode, volume):
        super().__init__(adrDest, adrExp, poids, expMode)
        self.volume = volume

    def calculTimbre(self):
        if self.expMode == "normal" or self.expMode == "Normal":
            return (0.25 * self.volume) * self.poids/1000
        elif self.expMode == "express" or self.expMode == "Express":
            # return (0.50 * self.volume) * (self.poids * 2.0)
            return (0.25 * self.volume * self.poids/1000) * 2.0

    def ToString(self):
        print("Colis: ")
        super().ToString()

        print("Volume: {}".format(self.volume))
        print("Prix du timbre: {}".format(self.calculTimbre()))
