def raise_to_a_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return raise_to_a_power(a ** 2, n // 2)
    else:
        return a * raise_to_a_power(a, n - 1)


number = float(input('Введите число: '))
power = int(input('Введите степень: '))
print(raise_to_a_power(number, power))