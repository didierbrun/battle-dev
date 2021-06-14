import sys
#
# Exercice n°2 - 3, 2, 1... Décollage !
#
input = open("../datas/exo2/input{}.txt".format(sys.argv[1]), "r").read().split()
output = open("../datas/exo2/output{}.txt".format(sys.argv[1]), "r").read()

pseudos = input[1:]
solution = None

for p in pseudos:
    if pseudos.count(p) == 2:
        solution = p

print ("-----------------------------")
print ("Exervice n°2")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(solution))
print ("Solution: {}".format(output))
print ("-----------------------------")