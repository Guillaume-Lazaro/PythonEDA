from CompteBancaire import *

## Exercice 1 sur Python
compte1 = CompteBancaire("Duchmol", 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()