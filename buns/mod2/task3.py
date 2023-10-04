s = input()
a = b = c = ''
space = 0
for i in s:
    if space == 0:
        a += i
    else if space == 1:
        b += i
    else:
        c += i
    if i == ' ':
        space += 1
a, b, c = int(a), int(b), int(c)
if a < b and a < c:
    if b < c:
        print(b)
    else:
        print(c)
if b < a and a < c:
    if a < c:
        print(a)
    else:
        print(c)
if c < b and c < a:
    if b < a:
        print(b)
    else:
        print(a)
