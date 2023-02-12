# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

from random import randint
N = int(input("Введите N: "))
int_array = [randint(1, N // 2) for _ in range(N)]
print(f"Массив случайных {N} чисел от 1 до {N // 2}")
print(int_array)
x = int(input("Введите x: "))
distances = {abs(x - num) for num in int_array}
min_dist = min(distances)
nearest_numbers = {num for num in int_array if abs(x - num) == min_dist}
print(f"Числа {nearest_numbers} являются ближайшими к числу {x} числами массива и находятся от него на расстоянии {min_dist}")


