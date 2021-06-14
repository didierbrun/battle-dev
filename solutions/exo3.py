import sys
#
# Exercice n°3 - Tetris Bot 1.0
#
input = list(map(list, open("../datas/exo3/input{}.txt".format(sys.argv[1]), "r").read().split()))
output = open("../datas/exo3/output{}.txt".format(sys.argv[1]), "r").read()

grid = input
grid += [['#' for i in range(10)]]

solution = 'NOPE'

for col in range(10):
    row = 0
    while grid[row][col] != '#':
        row += 1
    if row > 3:
        goodRows = 0
        for i in range(4):
            if grid[row - 1 - i].count('#') == 9: 
                goodRows += 1
        if goodRows == 4:
            solution = 'BOOM ' + str(col + 1)
            break

print ("-----------------------------")
print ("Exervice n°3")
print ("Dataset: {}".format(sys.argv[1]))
print ("Result: {}".format(solution))
print ("Solution: {}".format(output))
print ("-----------------------------")