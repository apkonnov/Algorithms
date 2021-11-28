# Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(1, 50) for i in range(30)]

d = {}
for key in a:
    val = d.setdefault(key, 0)
    d[key] = val + 1
max_val = max(d.values())
b = [key for key, val in d.items() if val == max_val]
b.sort()

print('Исходный массив')
print(a)
if len(b) > 1:
    print(f'В массиве {max_val} раз(а) встречаются числа ', *b)
else:
    print(f'В массиве {max_val} раз(а) встречается число ', *b)
