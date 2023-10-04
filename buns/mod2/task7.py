s = input()
countzero = 0
countone =0
for i in s:
    if s == '0':
        countzero += 1
    if s == '1':
        countone += 1
if countzero == countone:
    print("'yes'")
else:
    print("'no'")

