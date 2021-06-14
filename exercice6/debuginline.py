#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import math
import heapq

input = []
backup = []
for line in sys.stdin:
	input.append(line.rstrip('\n'))
	backup.append(input[len(input) - 1])
	
	
#
# Classes
#
class Planet:
    def __init__(self, y, x):
        global pWidth, pHeight, galaxy, planet, ores, structComps
        self.y = y
        self.x = x
        self.value = 0
        self.distance = math.inf
        self.bestPosition = None
        self.ratio = 0 
        for j in range(0, pHeight):
            for i in range(0, pWidth):
                if planet[j][i] == '*':
                    self.value += ores[galaxy[y + j][x + i]]



class Graphe:
    def __init__(self):
        global width, height
        self.planets = []
        self.parents = [[ None ] * width for i in range(height)]
        self.arcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.findPlanets()
        self.distance = None

    def applyDiskstra(self, y, x):
        global width, height, costs, galaxy, pWidth, pHeight
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
                if dx >= 0 and dx < width and dy >= 0 and dy < height:
                    cost = distance[cy][cx] + costs[galaxy[dy][dx]]
                    if cost < distance[dy][dx]:
                        distance[dy][dx] = cost
                        self.parents[dy][dx] = [cy, cx]
                        heapq.heappush(nodes, (cost, [dy, dx]))
                    
            
            visited[cy][cx] = True
        
        self.distance = distance

    def computePlanetScore(self):
        global pWith, pHeight, width, height, galaxy, structComps, costs, galaxy, startX, startY

        for p in self.planets:
            for y in range(0, pHeight):
                for x in range(0, pWidth):
                    dy = y + p.y
                    dx = x + p.x
                    if galaxy[dy][dx] in structComps:
                        for arc in self.arcs:
                            ty = dy + arc[0]
                            tx = dx + arc[1]
                            if tx >= 0 and ty >= 0 and tx < width and ty < height:
                                if self.distance[ty][tx] < p.distance:
                                    p.distance = self.distance[ty][tx]
                                    p.bestPosition = [ty, tx]
                
        
        for p in self.planets:
            p.distance *= 2
            by, bx = p.bestPosition
            p.distance -= costs[galaxy[by][bx]] 
            p.distance += costs[galaxy[startY][startX]]
    
    def debugSolution(self):
        global width, height, pWidth, pHeight, startX, startY, galaxy, structComps, days
        map = [[' '] * width for i in range(height)]
        

        for y in range(height):
            map[y][0] = '#'
            map[y][width - 1] = '1'
        for x in range(width):
            map[0][x] = '#'
            map[height-1][x] = '#'



        for p in self.planets:
            for y in range(pHeight):
                for x in range(pWidth):
                    dx = x + p.x
                    dy = y + p.y
                    if galaxy[dy][dx] in structComps:
                        map[dy][dx] = galaxy[dy][dx]
            by, bx = p.bestPosition
            map[by][bx] = '%'
            while bx != startX or by != startY:
                by, bx = self.parents[by][bx]
                map[by][bx] = '.'
         
        
        map[startY][startX] = "X"


        res = sorted(self.planets, key = lambda p:p.ratio, reverse = True)

        remain = days
        score = 0

        for i in range(30):
            remain -= res[i].distance * 2
            score += res[i].value
            print (remain, score)
            

  

       
        

        #for l in map:
        #    print(''.join(l))
    
    
    def resolveSolution(self):
        global days, backup
        sys.stderr.write("ICI -->\n")
        
        if len(self.planets) == 0:
            sys.stderr.write("\n".join(backup))
        
            
            
        p = []
        w = []
        for planet in self.planets:
            w.append(planet.distance)
            p.append(planet.value)

        t = [ [0] * days for i in range(len(p)) ]
        for i in range(len(p)):
            for c in range(days):
                if c >= w[i]:
                    t[i][c] = max(t[i-1][c], t[i-1][c - w[i]] + p[i])
                else:
                    t[i][c] = t[i - 1][c]
        
        return t[len(p) -1][days - 1]
        

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


height, width = map(int, input.pop(0).split())
galaxy = []
for i in range(0, height):
    galaxy.append(list(input.pop(0)))
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
graphe.computePlanetScore()
solution = graphe.resolveSolution()

print (solution)