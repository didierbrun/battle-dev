import sys
import math
import heapq
#
# Exercice n°6 - Expédition minière
#
input = open("../datas/exo6/input{}.txt".format(sys.argv[1]), "r").read().splitlines()
output = int(open("../datas/exo6/output{}.txt".format(sys.argv[1]), "r").read())

#
# Classes
#

# Classe utilitaire pour stocker une planète de la carte
class Planet:
    def __init__(self, y, x):
        global pWidth, pHeight, galaxy, planet, ores, structComps
        self.y = y                                      # Position de la planète sur la carte
        self.x = x                                  
        self.value = 0                                  # Valeur des minerais de la planète
        self.distance = math.inf                        # Distance (coût déplacement) de cette planète vers la base
        self.bestPosition = None                        # La meilleure position carte pour récolter les minerais de cette planète
        for j in range(0, pHeight):                     # On parcours ici les cases de la planête pour aditionner la valeur de ses minerais
            for i in range(0, pWidth):
                if planet[j][i] == '*':
                    self.value += ores[galaxy[y + j][x + i]]

# Classe utilitaire permettant de calculer la solution
class Graphe:
    def __init__(self):
        global width, height                            # Taille de la galaxy  
        self.planets = []                               # Tableau contenant les planets trouvées
        self.distance = None                            # Tableau qui contiendra les distances vers chaque case [y, x]
        self.arcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Direction des arcs possibles
        self.findPlanets()                              # On lance la routine pour trouver les planètes

    # Algorithme de Dijkstra, permet de trouver les distances optimales depui la base, vers toutes les cases de la carte
    def applyDijkstra(self, y, x):                          
        global width, height, costs, galaxy, pWidth, pHeight
        distance = [[math.inf] * width for i in range(height)]
        visited = [[False] * width for i in range(height)]
        distance[y][x] = 0
        nodes = [(0, [y, x])]

        # Utiliser un algo Heap Queue pour optimiser la recherche de la prochaine case à visiter 
        heapq.heapify(nodes)
        
        while (len(nodes) > 0):
            node = heapq.heappop(nodes)
            cy, cx = node[1]
            for arc in self.arcs:                                           # On parcours les 4 directions possibles
                dx = cx + arc[1]
                dy = cy + arc[0]
                if dx >= 0 and dx < width and dy >= 0 and dy < height:
                    cost = distance[cy][cx] + costs[galaxy[dy][dx]]         # On calcul le cout du sommet actuel + déplacement
                    if cost < distance[dy][dx]:                             # Si le cout est meilleur, on met à jour le sommet 
                        distance[dy][dx] = cost
                        heapq.heappush(nodes, (cost, [dy, dx]))
            visited[cy][cx] = True                                          # On marque la case comme visitée
        self.distance = distance

    # Cette méthode sert à parcourir toutes les planêtes et détermine quel distance minimale on peut parcourir pour récolter ses minerais
    def computePlanetScore(self):
        global pWith, pHeight, width, height, galaxy, structComps, costs, galaxy, startX, startY
        for p in self.planets:                                      # Parcours des planètes
            for y in range(0, pHeight): 
                for x in range(0, pWidth):
                    dy = y + p.y
                    dx = x + p.x
                    if galaxy[dy][dx] in structComps:               # Si l'élement visité est un élément structurel
                        for arc in self.arcs:                       # Parcours des 4 cases adjacentes
                            ty = dy + arc[0]
                            tx = dx + arc[1]
                            if tx >= 0 and ty >= 0 and tx < width and ty < height:  # Si la case visitée appartient à la planète
                                if self.distance[ty][tx] < p.distance:              # Si la distance en cette case est meilleure que la courante
                                    p.distance = self.distance[ty][tx]              # Sauvegarde la nouvelle distance
                                    p.bestPosition = [ty, tx]                       # Sauvegarde de la meilleure position
        
        # Une fois les meilleures distances trouvées, il faut compter le retour vers la base (*2)
        for p in self.planets:
            p.distance *= 2
            by, bx = p.bestPosition                         # Il faut retrancher la case d'arivée une fois
            p.distance -= costs[galaxy[by][bx]]             # et ajouter la case de départ une fois
            p.distance += costs[galaxy[startY][startX]]
    
    # Implémentation d'un Knacksack solver pour trouver la meilleure combinaison de planète possible (Problème du sac à dos)
    def resolveSolution(self):
        global days
        p = []
        w = []
        for planet in self.planets:         # Ce solver générique fonctionne avec 2 tableaux en entrée, les valueus, et les couts
            w.append(planet.distance)
            p.append(planet.value)

        t = [ [0] * days for i in range(len(p)) ]
        for i in range(len(p)):
            for c in range(days):
                if c >= w[i]:
                    t[i][c] = max(t[i-1][c], t[i-1][c - w[i]] + p[i])
                else:
                    t[i][c] = t[i - 1][c]

        # Il faut gérer le cas particulier ou une seule planète est présente 
        if len(p) == 1:
            if w[0] <= days:
                return p[0]
    
        return t[len(p) -1][days - 1]


    # Methode pour trouver les planètes de la galaxy selon leur pattern
    def findPlanets(self):
        global height, width, pHeight, pWidth, planet, galaxy, structComps
        pattern = ['' for i in range(height)]           # Pattern nettoyé de la galaxy
        patternPlanet = ['' for i in range(pHeight)]    # Pattern nettoyé de la planète

        # On reconstruit des pattern propre, qui ne comporte que les éléments structurels
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
        patternRow = 0

        # On va commencer par recherche une rangée du pattern avec au moins un signe distinctif 
        if pWidth > 1:
            while (patternPlanet[patternRow][0] * pWidth == patternPlanet[patternRow]):
                patternRow += 1

        # On parcours chaque rangée de la galaxy 
        for y in range(height - pHeight + 1 + patternRow):
            index = 0
            findX = pattern[y].find(patternPlanet[patternRow], index)       # On cherche la première occurence 
            while  findX != -1:                                             # Puis les suivantes, qu'on stocke dans un tableau 
                index = findX + 1
                candidates.append([y, findX])
                findX = pattern[y].find(patternPlanet[patternRow], index)

        for c in candidates:                                                # Pour chaque candidat trouée (une ranger qui match)
            cy, cx = c
            count = 0
            for y in range(pHeight):                                        # On teste également les autres rangée du pattern planète
                if pattern[y + cy - patternRow][cx : cx + pWidth] == patternPlanet[y]:
                    count += 1
            if count == pHeight:
                self.planets.append(Planet(cy - patternRow, cx))            # Si le nombre de rangée est OK, on sauve la planète

#
# Read datas
#
height, width = map(int, input.pop(0).split())          # Taille de la galaxy
galaxy = []                                             # Tableau contenant la galaxy
for i in range(0, height):                              
    galaxy.append(list(input.pop(0)))
pHeight, pWidth = map(int, input.pop(0).split())        # Taille des planètes
planet = []                                             # Pattern de le planète
for i in range(0, pHeight):     
    planet.append(input.pop(0))
countComp = int(input.pop(0))                           # Nombre de composants structurels
sComps = input.pop(0).split()               
structComps = {}    
for s in sComps:                                        # On stock les composant structurels dans un dictionnaire à clé
    structComps[s] = True
countOres = int(input.pop(0))                           # Nombre d'éléments organiques
ores = {}
costs = {}                                              # Dictionnaire de cout pour atteindre des cases avec cet élément
for i in range(0, countOres):
    parts = input.pop(0).split()
    ores[parts[0]] = int(parts[1])
for i in range(0, countComp + countOres):
    parts = input.pop(0).split()
    costs[parts[0]] = int(parts[1])
startY, startX = map(int, input.pop(0).split())         # Position de départ
days = int(input.pop(0))                                # Durée de la mission

#
# Resolve
#
graphe = Graphe()                                       # Construction du graphe de départ
graphe.applyDijkstra(startY, startX)                    # On applique l'algorithme de Disjkstra pour trouver les chemins
graphe.computePlanetScore()                             # On calcul les scores de récoltes optimaux vers les planètes
solution = graphe.resolveSolution()                     # On détermine la meilleure solution de récolte en fonction de la durée de la mission

#
# Output
#
print ("-----------------------------")
print ("Exercice n°6")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(solution))
print ("Solution: {}".format(output))
print ("-----------------------------")