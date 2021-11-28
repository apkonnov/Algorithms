# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-10, 10) for i in range(30)]

max_val = min(a)
assert max_val < 0, 'нет отрицательных элементов'
for val in a:
    if max_val < val < 0:
        max_val = val
b = [idx for idx, val in enumerate(a) if val == max_val]

print('Исходный массив')
print(a)
print(f'Максимальный отрицательный элемент = {max_val}, индекс(ы) = ', *b)
