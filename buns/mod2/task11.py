s = input()
secuence = s.replace(' ', '')
sWithouti = ''
for i in range(0,len(secuence)):
    sWithouti = secuence[:i] + secuence[i + 1:]
    if secuence[i] in sWithouti:
        print(secuence[i] in sWithouti)
        break
if secuence[i] not in sWithouti:
    print(secuence[i] in sWithouti) 
                  

