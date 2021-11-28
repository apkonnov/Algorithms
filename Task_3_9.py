# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

m = 5
n = 4
a = [[random.randint(0, 10) for j in range(m)] for i in range(n)]
b = [min([a[i][j] for i in range(n)]) for j in range(m)]

print('Исходная матрица')
for i in range(n):
    for j in range(m):
        print(a[i][j], end='\t')
    print()
print('Минимальные элементы столбцов матрицы')
for j in range(m):
    print(b[j], end='\t')
print()
print('Максимальный элемент среди минимальных элементов столбцов матрицы ')
print(max(b))
