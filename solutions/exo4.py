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

#
# Compter les debris d'une portion de la ceinture 
#
def countDebris(dic, f, l):
    global ceinture
    for c in ceinture[f:l]:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

#
# Comparer 2 portions de la ceinture 
#
def compare(a, b):
    for k, value in a.items():
        if not(k in b and b[k] == value // 2):
            return False
    return True

#
# Ajout d'un débris à la portion en cours
#
def addDebris(a, pos):
    global ceinture
    if ceinture[pos] in a:
        a[ceinture[pos]] += 1
    else:
        a[ceinture[pos]] = 1

#
# Retrait d'un débris à la portion en cours
#
def removeDebris(a, pos):
    global ceinture
    a[ceinture[pos]] -= 1

#
# Resolve
#
length = int(input.pop(0))                      # Taille de la ceinture
ceinture = input.pop(0)                         # Ceinture d'astéroides

initial = {}                                    # Portion courante
countDebris(initial, 0, length // 2)            # On compte les débris
total = copy.deepcopy(initial)                  # Somme totale (copie )
countDebris(initial, length // 2, length)       # On ajoute la seconde moitiée des débris

solution = 0                                    # Compteur de solutions trouvée

for i in range(0, length // 2):                 # On parcours toutes les coupes possible
    if compare(initial, total):                 # Si les sommes correspondent, on incrémente le compteur de solution
        solution += 1
    removeDebris(initial, i)                    # Retire le débris sortant dans la fenêtre glissante
    addDebris(initial, i + length // 2)         # Ajout du débris entrant dans la fenêtre glissante
    

print ("-----------------------------")
print ("Exervice n°4")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(solution * 2))
print ("Solution: {}".format(output))
print ("-----------------------------")