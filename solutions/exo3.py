import sys
#
# Exercice n°3 - Tetris Bot 1.0
#
input = list(map(list, open("../datas/exo3/input{}.txt".format(sys.argv[1]), "r").read().split()))
output = open("../datas/exo3/output{}.txt".format(sys.argv[1]), "r").read()

grid = input                            # Grille de jeu
grid += [['#' for i in range(10)]]      # On ajoute à la grille de jeu une dernière rangée pour simuler un plancher

solution = 'NOPE'                       # Solution par défaut

for col in range(10):                   # On parcours chaque colonne
    row = 0 
    while grid[row][col] != '#':        # On trouve le point libre le plus bas dans la colonne
        row += 1
    if row > 3:                         # Si le point bas est supérieur à 3 (car la barre fait 4 cases de haut)
        goodRows = 0
        for i in range(4):                              # On vérifie la colonne courante + les 3 du dessus
            if grid[row - 1 - i].count('#') == 9:       # Si la somme de # est 9, c'est que la rangée est pleine 
                goodRows += 1
        if goodRows == 4:                               # Si on a 4 rangées, pleine, le tétris est possible
            solution = 'BOOM ' + str(col + 1)
            break

print ("-----------------------------")
print ("Exervice n°3")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(solution))
print ("Solution: {}".format(output))
print ("-----------------------------")