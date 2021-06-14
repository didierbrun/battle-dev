from heapq import heappop, heappush

prime = 1000000007
a = 684515155
a1 = pow(a, prime-2, prime)

N1, N2 = [int(x) for x in input().split()]
C = []
for i in range(N1):
	C += [list(input())]
K1, K2 = [int(x) for x in input().split()]
P = []
for j in range(K1):
	P += [list(input())]

S = int(input())
structurels = set(input().split())

M = int(input())
minerais = dict()
for i in range(M):
	m, v = input().split()
	v = int(v)
	minerais[m] = v

duree = dict()
for i in range(M+S):
	c, v = input().split()
	v = int(v)
	duree[c] = v

x, y = [int(x) for x in input().split()]
D = int(input())

def valid(i,j):
	return (0<=i<N1 and 0<=j<N2)

#implementation using rolling hashes
#hash=sum(x*a^(K2*i+j))%prime
def patternMatching(C, P, structurels, minerais):
	N1, N2 = len(C), len(C[0])
	K1, K2 = len(P), len(P[0])
	P1 = [[P[i][j] if P[i][j] in structurels else chr(0) for j in range(K2)] for i in range(K1)]
	C1 = [[C[i][j] if C[i][j] in structurels else chr(0) for j in range(N2)] for i in range(N1)]

	refhash = sum(ord(P1[i][j]) * pow(a, K2*i + j, prime) for i in range(K1) for j in range(K2))%prime

	hash1d = []
	for i in range(N1):
		hash1d += [[sum(ord(C1[i][j]) * pow(a, j, prime) for j in range(K2))%prime]]
		for j in range(K2, N2):
			hash1d[i] += [((hash1d[i][-1]-ord(C1[i][j-K2]))*a1+ord(C1[i][j])*pow(a, K2-1, prime))%prime]

	hash2d = [[0 for j in range(K2, N2+1)] for i in range(K1, N1+1)]
	for j in range(K2, N2+1):
		hash2d[0][j-K2] = sum(hash1d[i][j-K2] * pow(a, i*K2, prime) for i in range(K1))%prime
	for i in range(K1, N1):
		for j in range(K2, N2+1):
			hash2d[i-K1+1][j-K2] = ((hash2d[i-K1][j-K2]-hash1d[i-K1][j-K2])*pow(a1, K2, prime)+hash1d[i][j-K2]*pow(a, K2*(K1-1), prime))%prime
			
	zones_minage = [[set() for j in range(N2)] for i in range(N1)]
	valeurs = []
	nb_planetes = 0
	for i in range(N1+1-K1):
		for j in range(N2+1-K2):
			if hash2d[i][j] == refhash and P1==[aux[j:j+K2] for aux in C1[i:i+K1]]:
				valeur = 0
				for k in range(K1):
					for(l) in range(K2):
						if P[k][l] == '*':
							valeur += minerais[C[i+k][j+l]]
						elif P[k][l] != '-':
							for di,dj in [(-1,0), (1,0), (0,-1), (0,1)]:
								if valid(i+k+di, j+l+dj):
									zones_minage[i+k+di][j+l+dj] |= {nb_planetes}
				nb_planetes += 1
				valeurs += [valeur]
	return zones_minage, valeurs


def Dijkstra(C, x, y, duree, zones_minage, nb_planetes):
	N1, N2 = len(C), len(C[0])
	aVoir = [(-duree[C[x][y]],x,y)]
	dist = [[-1 for j in range(N2)] for i in range(N1)]
	distances = [float('inf') for i in range(nb_planetes)]
	while aVoir != []:
		d, i, j = heappop(aVoir)
		if valid(i,j) and dist[i][j] == -1:
			dist[i][j] = d
			for di,dj in [(-1,0), (1,0), (0,-1), (0,1)]:
				heappush(aVoir, (d+2*duree[C[i][j]], i+di, j+dj))
			for p in zones_minage[i][j]:
				distances[p] = min(distances[p], d+duree[C[i][j]])
	return distances
			

def KP(valeurs, distances, D):
	max_valeur = [0 for d in range(D+1)]
	nb_planetes = len(valeurs)
	for i in range(nb_planetes):
		for d in range(D, distances[i]-1, -1):
			max_valeur[d] = max(max_valeur[d], max_valeur[d-distances[i]] + valeurs[i])
	return max_valeur[D]

zones_minage, valeurs = patternMatching(C,P,structurels, minerais)
distances = Dijkstra(C, x, y, duree, zones_minage, len(valeurs))
print(KP(valeurs, distances, D))
