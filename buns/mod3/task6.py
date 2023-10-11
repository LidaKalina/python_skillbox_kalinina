s = input().split()
result = [s[i][-1] for i in range(len(s))]
print(''.join(result))

