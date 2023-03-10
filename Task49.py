# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию f ind_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж
# из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти
# эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий
# такую  площадь. Гарантируется, что самая далекая планета ровно одна.
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
one_lst, two_lst = zip(*orbits)
my_list = []
for i in range(len(one_lst)):
    if one_lst[i]== two_lst[i]:
        my_list.append(0)
    else:
        s = one_lst[i]* two_lst[i]
        my_list.append(s)

for i in range(len(one_lst)):
    if my_list[i] == max(my_list):
        print(orbits[i])

max_elem = max(my_list)
i_max_elem = my_list.index(max_elem)
print(orbits[i_max_elem])