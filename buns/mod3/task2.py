s = int(input())
print('' if s < 0 else ', '.join([bin(s)[2:], oct(s)[2:], hex(s)[2:]]))
