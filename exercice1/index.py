import sys
#
# Exercice n°1 - Préparation minitieuse
#
input = map(int, open("./exercice1/datas/input{}.txt".format(sys.argv[1]), "r").read().split())
output = int(open("./exercice1/datas/output{}.txt".format(sys.argv[1]), "r").read())

ergoPerUa = 5
ergolMass, distance = input
mass = ergolMass + distance * ergoPerUa

print ("-----------------------------")
print ("Exervice n°1")
print ("Dataset: {}".format(sys.argv))
print ("Result: {}".format(mass))
print ("Solution: {}".format(output))
print ("-----------------------------")