data = input()
s = ''
i = ''
space = 0
for j in data:
    if space == 0:
        s += j
    else:
        i += j
    if j == ',' or j == ' ':
        space += 1
count = 0
for k in s:
    if k == i:
        count += 1
    if k != i:
        print(count)
        break
