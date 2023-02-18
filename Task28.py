# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# def sum(a, b):
#     if a == 0:
#         return b
#     return sum(a - 1, b + 1)



# x1 = int(input("Введите число a: "))
# x2 = int(input("Введите число b: "))

def sum_numbers(max1, min1):
    if min1 > 0:
        max1 = sum_numbers(max1 + 1, min1 - 1)
    return max1


a1 = int(input('Введите первое число: '))
b1 = int(input('Введите второе число: '))

print('Сумма чисел =', sum_numbers(max(a1, b1), min(a1, b1)))