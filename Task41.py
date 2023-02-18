# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:
# 5
# 12345
# Вывод:
# 0
# Ввод:
# 5
# 15151
# Вывод:
# 2
# (каждое число вводится с новой строки)

# numm_list = [int(input(f'Введите {i + 1}-е число: ')) for i in range(int(input("Введите количество элементов массива N: ")))]
# print(numm_list)
# test_trio = []
# count = 0
# for i in range(len(numm_list) - 2):
#     test_trio = numm_list[i: i + 3]
#     if test_trio[0] < test_trio[1] > test_trio[2]:
#         count +=1
# print(count)

arr = list(int(input(f"Enter {i+1} your num:")) for i in range(int(input("Enter num len:"))))
n=len(arr)
result = 0
for i in range(1,n-1):
    if arr[i+1] < arr[i] > arr[i-1]:
        result += 1
print(f'Кол-во парных элементов списка = {result}')

