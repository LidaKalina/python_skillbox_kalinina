def letter_statistics(string):
    letter_dict = dict()
    ignor_char = ['`', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                  '=', '+', '№', '[', ']', '{', '}', '\\', '|', '/', '?', '.',
                  ',', '>', '<', ' ', '"', "'", '\n']
    for char in string:
        if char not in ignor_char:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
        else:
            continue

    return letter_dict


file_name = input()
f = open(file_name)
text = f.read()
result = letter_statistics(text)
sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
print(sorted_result)