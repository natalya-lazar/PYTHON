# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# from random import randint
# N = int(input("Введите длину последовательности N: "))
# my_list = [randint(1, 100) for i in range(N)]
# print(my_list)

# k = int(input("Введите значение k: "))
# while k > 0:                        # for i in range(k):
#     my_list.append(my_list[0])      #     my_list.append(my_list[0])
#     my_list.remove(my_list[0])      #     my_list.remove(my_list[0])
#     k -= 1
# print(my_list)

your_list = [int(input("Введите элемент: ")) for i in range(int(input("Введите длину последовательности N: ")))]
k = int(input("Введите значение k: ")) % len(your_list)
print(your_list)
k_list = your_list[k:] + your_list[:k]
print(k_list)