class Point:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Surcharge de l'opérateur
    def __str__(self):
        if self.z == 0:
            return "P({} , {})".format(self.x, self.y)
        else:
            return "P({} , {} , {})".format(self.x, self.y, self.z)

    def ToString(self):
        print(self)