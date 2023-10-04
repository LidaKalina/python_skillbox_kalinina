s = input()
a = ''
b = ''
space = 0
for i in s:
    if space == 0:
        a += i
    else:
        b += i
    if i == ' ':
        space += 1
a = int(a)
b = int(b)
print(a % b)
