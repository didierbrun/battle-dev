import sys
from operator import sub
import math

#
# Exercice n°5 - Ceinture d'astéroïdes
#
input = open("./exercice5/datas/input{}.txt".format(sys.argv[1]), "r").read().splitlines()
output = open("./exercice5/datas/output{}.txt".format(sys.argv[1]), "r").read()

#
# Classes
#
class Sommet:
    def __init__(self):
        self.on = None
        self.off = None
        self.absorb = 0
        self.maxDebris = 0

class Dijkstra:
    @classmethod
    def visitSommet(cls, sommet):
        sommet.off.maxDebris = max(sommet.off.maxDebris, sommet.maxDebris)
        sommet.on.maxDebris = max(sommet.on.maxDebris, sommet.maxDebris + sommet.absorb)
        return

        
#
# Resolution
#
length, duration, locked = map(int, input[0].split())
asteroids = list(map(int, input[1].split()))

sommets = []
absorb = sum(asteroids[0:duration])

#
# Construction de l'arbre
#
for i in range(0, length + locked + duration):
    s = Sommet()
    s.absorb = absorb
    sommets.append(s)
    absorb -= 0 if i >= length else asteroids[i]
    absorb += 0 if i + duration >= length else asteroids[i + duration]

#
# Affectation des arcs orientés
#
for i in range(0, length):
    sommets[i].off = sommets[i + 1]
    sommets[i].on = sommets[i + duration + locked]

#
# Caulcu du chemin le plus optimisé
#
for i in range(0, length):
    Dijkstra.visitSommet(sommets[i])

#
# Recherche du sommet avec le meilleur score
#
solution = 0
for i in range(0, len(sommets)):
    if sommets[i].maxDebris > solution:
        solution = sommets[i].maxDebris


print ("-----------------------------")
print ("Exervice n°5")
print ("Dataset: {}".format(sys.argv))
print ("Result: {}".format(sum(asteroids) - solution))
print ("Solution: {}".format(output))
print ("-----------------------------")