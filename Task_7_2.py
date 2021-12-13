# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


# слияние двух отсортированных массивов
def merge(lst_1, lst_2):
    lst = []
    i = 0
    j = 0
    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] <= lst_2[j]:
            lst.append(lst_1[i])
            i += 1
        else:
            lst.append(lst_2[j])
            j += 1
    while i < len(lst_1):
        lst.append(lst_1[i])
        i += 1
    while j < len(lst_2):
        lst.append(lst_2[j])
        j += 1
    return lst


# рекурсия
def merge_sort_recursive(lst):
    if len(lst) > 1:
        lst_1 = merge_sort_recursive(lst[:len(lst) // 2])
        lst_2 = merge_sort_recursive(lst[len(lst) // 2:])
        lst = merge(lst_1, lst_2)
    return lst


# итерация
def merge_sort_iterative(lst_1):
    lst_1 = [[item] for item in lst_1]
    while len(lst_1) > 1:
        m = len(lst_1) // 2
        lst_2 = []
        for i in range(m):
            lst_2.append(merge(lst_1[2*i], lst_1[2*i+1]))
        if len(lst_1) % 2 == 1:
            lst_2.append(lst_1[-1])
        lst_1 = lst_2
    return lst_1[0]


b = [random.randint(0, 49) for i in range(21)]
print('исходный массив         ', b)
print('отсортированный рекурсия', merge_sort_recursive(b))
print('отсортированный итерация', merge_sort_iterative(b))
