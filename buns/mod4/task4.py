def check_for_palindrome(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    odd_count = 0
    for count in letter_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return 'Из данного слова невозможно составить палиндром.'
    else:
        palindrome = ""

        for letter, count in letter_count.items():
            palindrome += letter * (count // 2)

        for letter, count in letter_count.items():
            if count % 2 != 0:
                palindrome += letter

        palindrome += palindrome[::-1]
        return palindrome


string = input("Введите слово: ").lower().replace(' ', '')
print(check_for_palindrome(string))
