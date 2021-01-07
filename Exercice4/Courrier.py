class Courrier:

    def __init__(self, adrDest, adrExp, poids, expMode):
        self.adrDest = adrDest
        self.adrExp = adrExp
        self.poids = poids
        self.expMode = expMode

    def ToString(self):
        print("Adresse destination: {}".format(self.adrDest))
        print("Adresse expédition: {}".format(self.adrExp))
        print("Poids: {} grammes".format(self.poids))
        print("Mode: {}".format(self.expMode))