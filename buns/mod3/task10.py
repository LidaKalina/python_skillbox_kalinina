size = int(input())
matrix = [['*'] * size for i in range(size)]
Tmatrix = [['*'] * size for i in range(size)]

for i in  range(size):
    for j in range(size):
        matrix[i][j] = j + 1
for i in  range(size):
    for j in range(size):
        Tmatrix[j][i] = j + 1

for row in matrix:
    print(', '.join(list(map(str, row))))
print('')    
for row in Tmatrix:
    print(', '.join(list(map(str, row))))
