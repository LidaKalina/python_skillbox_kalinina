def finde_gcd(a, b):
    if b == 0:
        return a
    else:
        return finde_gcd(b, a % b)


a, b = [float(i) for i in input('Введите числа: ').split()]
print("Наибольший общий делитель:", finde_gcd(a, b))
