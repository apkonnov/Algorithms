# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(0, 100) for i in range(20)]

min_idx = a.index(min(a))
max_idx = a.index(max(a))
start_idx = min_idx + 1 if min_idx < max_idx else max_idx + 1
stop_idx = max_idx if max_idx > min_idx else min_idx

print('Исходный массив')
print(a)
print('Сумма элементов, находящихся между минимальным и максимальным элементами = ', sum(a[start_idx:stop_idx]))
