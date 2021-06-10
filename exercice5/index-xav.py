import sys
from operator import sub
import math

#
# Exercice n°5 - Ceinture d'astéroïdes
#
input = open("./exercice5/datas/input{}.txt".format(sys.argv[1]), "r").read().splitlines()
output = open("./exercice5/datas/output{}.txt".format(sys.argv[1]), "r").read()

#
# Methods utils
#
def max_in_range(datas, r):
    maxValue = - math.inf
    maxIndex = None
    for i in range(r[0], r[1]):
        if i >=0 and i < len(datas) and datas[i] > maxValue:
            maxValue = datas[i]
            maxIndex = i
    return maxIndex

#
# Resolution
#
length, duration, locked = map(int, input[0].split())
asteroids = list(map(int, input[1].split()))

cumulM = sum(asteroids[0:duration])
cumulN = sum(asteroids[duration:duration + locked])

listM = []
listN = []

for i in range(0, len(asteroids)):
    listM.append(cumulM)
    listN.append(cumulN)

    cumulM -= asteroids[i] 
    cumulM += asteroids[i + duration] if i + duration < length else 0 


    cumulN -= asteroids[i - locked] if i - locked >= 0 else 0
    cumulN -= asteroids[i + duration] if i + duration < length else 0

    cumulN += asteroids[i + duration + locked] if i + duration + locked < length else 0
    cumulN += asteroids[i]

gain = list(map(sub, listM, listN))

indexes = []

index = 0
total = 0

while index < length:
    maxIndex = max_in_range(gain, (index, index + duration + locked))
    indexes.append(maxIndex)
    total += listM[maxIndex]
    index = maxIndex + duration + locked

print ("-----------------------------")
print ("Exervice n°5")
print ("Column M : ", listM)
print ("Column N : ", listN)
print ("Column O : ", gain)
print ("Solution indexes : ", indexes)
print ("Dataset: {}".format(sys.argv))
print ("Result: {}".format(sum(asteroids) - total))
print ("Solution: {}".format(output))
print ("-----------------------------")