from DateNaissance import *
from Personne import *
from Employe import *
from Chef import *

P = Personne("Ilyass","Math",DateNaissance(1,7,1982))
P.afficher()

E = Employe("Ilyass","Math",DateNaissance(1,7,1985),7865.548)
E.afficher()

Ch = Chef("Dupont","Paul",DateNaissance(13,10,1993),1150.0, "RH")
Ch.afficher()