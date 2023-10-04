s = input()
summodd = 0
summeven = 0
for i in range(0, len(s), 2):
    summodd += int(s[i])
for j in range(1, len(s), 2):
    summeven += int(s[j])
if (summodd + summeven * 3) % 10 == 0:
    print("yes")
else:
    print("no")

