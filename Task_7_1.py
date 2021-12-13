# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def bubble_sort_1(b):
    len_b = len(b)
    for i in range(len_b-1):
        for j in range(len_b-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
    return b


# убираем возможные лишние проходы
def bubble_sort_2(b):
    len_b = len(b)
    i = 0
    flag = True
    while i < len_b-1 and flag:
        flag = False
        for j in range(len_b-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                flag = True
        i += 1
    return b, i


a = [random.randint(-100, 99) for i in range(40)]
print(*a)
a1 = bubble_sort_1(a.copy())
print('i1 =', len(a)-1)
print(*a1)
a2, i2 = bubble_sort_2(a.copy())
print('i2 =', i2)
print(*a2)
