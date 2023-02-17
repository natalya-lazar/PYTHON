# Последовательностью Фибоначчи называется последовательность чисел
# a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)
x = int(input("Введите номер числа Фибоначчи: "))
# for i in range(x):
#     num_fib = fibonacci_of(i)
#     print(i + 1, "-", num_fib)

print(x, "число Фибоначчи - ", fibonacci_of(x - 1))

