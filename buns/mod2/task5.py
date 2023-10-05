s = input()
i = ''
num = ''
space = 0
for j in s:
    if space == 0 and j != ',':
        i += j
    elif space != 0 and j != ',':
        num += j
    if j == ',':
        space += 1
n = int(num)
print(i)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
indexi = alphabet.find(i)
print(indexi)
result = alphabet[indexi + n]
print(result)
