def check_numbers(numbers):
    unique_numbers = set(numbers)
    
    if len(unique_numbers) == 1:
        return "Все числа равны"
    elif len(unique_numbers) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"


data = [int(i) for i in input().split(' ')]
print(check_numbers(data))
