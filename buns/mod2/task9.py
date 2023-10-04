s = input()
countVowels = 0
countConsonants = 0
for i in s:
    if i in 'ёуеыаоэяию':
        countVowels += 1
    elif i in 'йцкнгшщзхфвпрлджчсмтб':
        countConsonants += 1
print(countVowels, countConsonants)
