import sys
import math
import copy
import heapq
from itertools import combinations

#
# Exercice n°6 - Expédition minière
#

#
# Classes
#
class Planet:
    def __init__(self, y, x):
        global pWidth, pHeight, galaxy, planet, ores, structComps
        self.y = y
        self.x = x
        self.value = 0
        for j in range(0, pHeight):
            for i in range(0, pWidth):
                if planet[j][i] == '*':
                    self.value += ores[galaxy[y + j][x + i]]



class Graphe:
    def __init__(self):
        global width, height
        self.planets = []
        self.arcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.findPlanets()

        print("Planets founds : ", len(self.planets))

    def applyDiskstra(self, y, x):
        global width, height, costs, galaxy
        distance = [[math.inf] * width for i in range(height)]
        visited = [[False] * width for i in range(height)]
        distance[y][x] = 0
        nodes = [(0, [y, x])]
        heapq.heapify(nodes)
        
        while (len(nodes) > 0):
            node = heapq.heappop(nodes)
            cy, cx = node[1]
            for arc in self.arcs:
                dx = cx + arc[1]
                dy = cy + arc[0]
                if dx >= 0 and dx < width and dy >= 0 and dy < height and visited[dy][dx] == False:
                    cost = distance[cy][cx] + costs[galaxy[dy][dx]]
                    if cost < distance[dy][dx]:
                        distance[dy][dx] = cost
                        heapq.heappush(nodes, (cost, [dy, dx]))
            
            visited[cy][cx] = True
        





    def debugMap(self, datas):
        for l in datas:
            print(l)

    def findPlanets(self):
        global height, width, pHeight, pWidth, planet, galaxy, structComps
        pattern = ['' for i in range(height)]
        patternPlanet = ['' for i in range(pHeight)]

        for y in range(pHeight):
            for x in range(pWidth):
                if planet[y][x] in structComps:
                    patternPlanet[y] += planet[y][x]
                else:
                    patternPlanet[y] += ' '

        for y in range(height):
            for x in range(width):
                if galaxy[y][x] in structComps:
                    pattern[y] += galaxy[y][x]
                else:
                    pattern[y] += ' '

        candidates = []

        for y in range(height - pHeight + 1):
            index = 0
            findX = pattern[y].find(patternPlanet[0], index)
            while  findX != -1:
                index = findX + pWidth
                candidates.append([y, findX])
                findX = pattern[y].find(patternPlanet[0], index)


        for c in candidates:
            cy, cx = c
            count = 0
            for y in range(pHeight):
                if pattern[y + cy][cx : cx + pWidth] == patternPlanet[y]:
                    count += 1
            if count == pHeight:
                self.planets.append(Planet(cy, cx))




            

       
                


#
# Read datas
#
input = open("./exercice6/datas/input{}.txt".format(sys.argv[1]), "r").read().splitlines()
output = int(open("./exercice6/datas/output{}.txt".format(sys.argv[1]), "r").read())

height, width = map(int, input.pop(0).split())
galaxy = []
for i in range(0, height):
    galaxy.append(input.pop(0))
pHeight, pWidth = map(int, input.pop(0).split())
planet = []
for i in range(0, pHeight):
    planet.append(input.pop(0))
countComp = int(input.pop(0))
sComps = input.pop(0).split()
structComps = {}
for s in sComps: 
    structComps[s] = True
countOres = int(input.pop(0))
ores = {}
costs = {}
for i in range(0, countOres):
    parts = input.pop(0).split()
    ores[parts[0]] = int(parts[1])
for i in range(0, countComp + countOres):
    parts = input.pop(0).split()
    costs[parts[0]] = int(parts[1])
startY, startX = map(int, input.pop(0).split())
days = int(input.pop(0))

#
# Resolve
#
graphe = Graphe()
graphe.applyDiskstra(startY, startX)
#graphe.findBestPlanets()
#solution = graphe.computeSolution()

#
# Output
#
print ("-----------------------------")
print ("Exercice n°6")
print ("Dataset: {}".format(sys.argv[1]))
#print ("Result: {}".format(solution))
print ("Solution: {}".format(output))
print ("-----------------------------")