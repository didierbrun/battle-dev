import sys
#
# Exercice n°1 - Préparation minitieuse
#
input = map(int, open("../datas/exo1/input{}.txt".format(sys.argv[1]), "r").read().split())
output = int(open("../datas/exo1/output{}.txt".format(sys.argv[1]), "r").read())

ergoPerUa = 5                               # Ergo par unité astronomique
ergolMass, distance = input                 # Ergo au décollage
mass = ergolMass + distance * ergoPerUa     # La solutione est la quantité d'ergo au décollage + la distance * consommation

print ("-----------------------------")
print ("Exervice n°1")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(mass))
print ("Solution: {}".format(output))
print ("-----------------------------")