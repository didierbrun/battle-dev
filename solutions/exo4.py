import sys
import copy

#
# Exercice n°4 - Nettoyeur de l'espace
#
input = open("../datas/exo4/input{}.txt".format(sys.argv[1]), "r").read().splitlines()
output = open("../datas/exo4/output{}.txt".format(sys.argv[1]), "r").read()

#
# Methods
#
def countDebris(dic, f, l):
    global ceinture
    for c in ceinture[f:l]:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

def compare(a, b):
    for k, value in a.items():
        if not(k in b and b[k] == value // 2):
            return False
    return True

def addDebris(a, pos):
    global ceinture
    if ceinture[pos] in a:
        a[ceinture[pos]] += 1
    else:
        a[ceinture[pos]] = 1

def removeDebris(a, pos):
    global ceinture
    a[ceinture[pos]] -= 1

#
# Resolve
#
length = int(input.pop(0))
ceinture = input.pop(0)

initial = {}
countDebris(initial, 0, length // 2)
total = copy.deepcopy(initial)
countDebris(initial, length // 2, length)

solution = 0

for i in range(0, length // 2):
    if compare(initial, total):
        solution += 1
    removeDebris(initial, i)
    addDebris(initial, i + length // 2)
    

print ("-----------------------------")
print ("Exervice n°4")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(solution * 2))
print ("Solution: {}".format(output))
print ("-----------------------------")