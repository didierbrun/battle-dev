import sys
#
# Exercice n°2 - 3, 2, 1... Décollage !
#
input = open("../datas/exo2/input{}.txt".format(sys.argv[1]), "r").read().split()
output = open("../datas/exo2/output{}.txt".format(sys.argv[1]), "r").read()

pseudos = input[1:]             # Liste des pseudos
solution = None                 # La solution trouvée

for p in pseudos:               # On parcours les pseudos
    if pseudos.count(p) == 2:   # Si le pseudo existe 2 fois...
        solution = p            # ... c'est la solution

print ("-----------------------------")
print ("Exervice n°2")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(solution))
print ("Solution: {}".format(output))
print ("-----------------------------")