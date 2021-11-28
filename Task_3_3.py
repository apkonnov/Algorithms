# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(1, 100) for i in range(20)]

max_a = max(a)
min_a = min(a)

print('Максиальный элемент = ', max_a)
print('Минимальный элемент = ', min_a)
print('Исходный массив')
print(a)

for idx, val in enumerate(a):
    if val == min_a:
        a[idx] = max_a
    if val == max_a:
        a[idx] = min_a

print('Измененный массив')
print(a)
