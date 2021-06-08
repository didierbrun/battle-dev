import sys
from collections import Counter
#
# Exercice n°2 - 3, 2, 1... Décollage !
#
input = open("./exercice2/datas/input{}.txt".format(sys.argv[1]), "r").read().split()
output = open("./exercice2/datas/output{}.txt".format(sys.argv[1]), "r").read()

pseudos = input[1:]
solution = None

for p in pseudos:
    if pseudos.count(p) == 2:
        solution = p

print ("-----------------------------")
print ("Exervice n°2")
print ("Dataset: {}".format(sys.argv))
print ("Result: {}".format(solution))
print ("Solution: {}".format(output))
print ("-----------------------------")