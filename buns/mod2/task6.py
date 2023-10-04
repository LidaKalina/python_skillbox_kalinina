s = input()
result = ''
for i in range(len(s)-1, -1, -1) :
    if s[i] == '.':
        print(result)
        result = ''
    if s[i] != '.':
        result = s[i] + result
print(result)

