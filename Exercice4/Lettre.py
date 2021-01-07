from Courrier import *

class Lettre(Courrier):

    def __init__(self, adrDest, adrExp, poids, expMode, format):
        super().__init__(adrDest, adrExp, poids, expMode)
        self.format = format

    def calculTimbre(self):
        tarifDeBase = 0
        if self.format == "A4":
            tarifDeBase = 2.50
        elif self.format == "A3":
            tarifDeBase = 3.50

        if self.expMode == "normal" or self.expMode == "Normal":
            return tarifDeBase * (self.poids/1000)
        elif self.expMode == "express" or self.expMode == "Express":
            return tarifDeBase * (2.0 * (self.poids/1000))

    def ToString(self):
        print("Lettre: ")
        super().ToString()

        print("Format: {}".format(self.format))
        print("Prix du timbre: {}".format(self.calculTimbre()))