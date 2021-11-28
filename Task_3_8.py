# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять
# сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.

import random

m = 5
n = 4
a = []
for i in range(n):
    b = []
    for j in range(m - 1):
        b.append(random.randint(0, 10))
    b.append(0)
    a.append(b)

print('Исходная матрица')
for i in range(n):
    for j in range(m):
        print(a[i][j], end='\t')
    print()

for i in range(n):
    a[i][m-1] = sum(a[i])

print('Полученная матрица')
for i in range(n):
    for j in range(m):
        print(a[i][j], end='\t')
    print()
