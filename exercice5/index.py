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
    #
    # Le Sommet représente une position dans le temps pour laquelle il est possible de faire le choix d'activer ou non le bouclier
    #
    def __init__(self):
        self.on = None      # Arc vers un sommet en cas de non-activation du bouclier
        self.off = None     # Arc vers un sommet en cas d'activation du bouclier
        self.absorb = 0     # Absorbtion des dévris en cas d'activation du bouclier
        self.maxDebris = 0  # Absorption cumulée des débris 

class Dijkstra:
    @classmethod
    def visitSommet(cls, sommet):
        sommet.off.maxDebris = max(sommet.off.maxDebris, sommet.maxDebris)                  # Relâchement de l'arc off
        sommet.on.maxDebris = max(sommet.on.maxDebris, sommet.maxDebris + sommet.absorb)    # Relâchement de l'arc on
        return

        
#
# Récupération des variables d'entrée du problème
#
length, duration, locked = map(int, input[0].split())
asteroids = list(map(int, input[1].split()))

# Création d'un tableau pour stocker le graphe
sommets = []

# Calcul de la première fenêtre d'aborption
absorb = sum(asteroids[0:duration])

#
# Construction de l'arbre
#
for i in range(0, length + locked + duration):
    # Ajoute d'un nouveau sommet vierge au Graphe
    s = Sommet()

    # Fenêtre glissante pour calculer toutes les aborbtions de chaque index
    s.absorb = absorb
    sommets.append(s)
    absorb -= 0 if i >= length else asteroids[i]
    absorb += 0 if i + duration >= length else asteroids[i + duration]

#
# Affectation des arcs orientés
#
for i in range(0, length):
    sommets[i].off = sommets[i + 1]                 # En cas de non-activation du bouclier, on se rend au noeud d'index suivant
    sommets[i].on = sommets[i + duration + locked]  # En cas d'activation du bouclier, on se rend au noeud d'index courant + duration + locked

#
# Calcul du chemin le plus optimisé
#
for i in range(0, length):
    # Version simplifié de l'algorithme de Dijkstra
    Dijkstra.visitSommet(sommets[i])

#
# Recherche du sommet avec le meilleur score cumulé
#
solution = 0
for i in range(0, len(sommets)):
    if sommets[i].maxDebris > solution:
        solution = sommets[i].maxDebris


print ("-----------------------------")
print ("Exervice n°5")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(sum(asteroids) - solution))
print ("Solution: {}".format(output))
print ("-----------------------------")