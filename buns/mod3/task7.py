s = input().replace(' ', '')
result = [s.count(i)>= 2 for i in s]
print(any(result))

