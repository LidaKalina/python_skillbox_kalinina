def get_armstrong_numbers():
    num = 10
    while True:
        power = len(str(num))
        sum_of_powers = sum([int(digit)**power for digit in str(num)])
        if sum_of_powers == num:
            yield num
        num += 1


for i, armstrong_number in enumerate(get_armstrong_numbers(), start=1):
    print(armstrong_number, end=' ')
    if i == 8:
        break