# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


# Массив размером 2m + 1
def median_sorted(ls):
    return sorted(ls)[len(ls) // 2]


def median(ls):
    lst = ls.copy()
    idx = len(a) // 2
    pivot = random.choice(lst)
    while len(lst) > 1:
        lst_left = [item for item in lst if item < pivot]
        lst_pivot = [item for item in lst if item == pivot]
        lst_right = [item for item in lst if item > pivot]
        if idx < len(lst_left):
            lst = lst_left
        elif idx < len(lst_left) + len(lst_pivot):
            lst = lst_pivot
            return lst[0]
        else:
            lst = lst_right
            idx = idx - len(lst_left) - len(lst_pivot)
        pivot = random.choice(lst)
    return lst[0]


a = [random.randint(0, 99) for i in range(27)]
print('исходный массив       ', a)
print('отсортированный массив', sorted(a))
print('медиана  с сортировкой ', median_sorted(a.copy()))
print('медиана без сортировки ', median(a))
