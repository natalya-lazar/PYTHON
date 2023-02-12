# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

Решение 1:
from random import randint
my_list = [randint(-10, 10) for _ in range(randint(1, 10))]

counter = 0
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        counter += 1
print(counter)

Решение 2:
from random import randint
my_list = [randint(-10, 10) for _ in range(randint(1, 10))]

new_list = [1 for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(len(new_list))


Решение 3:
def count_larger_then_previous(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
    return count

array = [0, -1, 5, 2, 3]
print(count_larger_then_previous(array))
