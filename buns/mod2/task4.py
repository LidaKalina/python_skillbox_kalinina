s = int(input())
if s <= 0:
    print('"Неверный ввод"')
else:
    i = s
    bins = ''
    while i > 0:
        bins = str(i % 2) + bins
        i = i // 2
    j = s
    octs = ''
    while j > 0:
        octs = str(j % 8) + octs
        j = j // 8
    k = s
    hexs = ''
    while k > 0:
        hexs = str(k % 16) + hexs
        k = k // 16
    print(bins, octs, hexs)   

