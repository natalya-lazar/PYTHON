# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета

# Примеры:
# 385916 -> yes
# 123456 -> no

n = int(input("Введите число - "))
n6 = n % 10
n5 = (n % 100 - n6) // 10
n4 = (n % 1000 - n5 *10 - n6) // 100
n1 = n // 100000
n2 = n // 10000 - 10 * n1
n3 = n // 1000 - 100 * n1 - 10 * n2
if (n1 + n2 + n3) == (n4 + n5 + n6):
    print("YES")
else:
    print("NO")