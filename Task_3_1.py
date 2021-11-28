# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
# в диапазоне от 2 до 9.

a1 = 2
a2 = 100
b1 = 2
b2 = 10

# вариант с переменными
for i in range(b1, b2):
    cnt = 0
    for n in range(a1, a2):
        if n % i == 0:
            cnt += 1
    print(f'на {i} делится {cnt} чисел')
print()

# вариант со списками
for i in range(b1, b2):
    b = [n for n in range(a1, a2) if n % i == 0]
    print(f'на {i} делится {len(b)} чисел из заданного диапазона')
print()

# вариант со словарем
d = {}
for key in range(b1, b2):
    val = d.setdefault(key, 0)
    for n in range(a1, a2):
        if n % key == 0:
            val += 1
    d[key] = val
for key, val in d.items():
    print(f'на {key} делится {val} чисел')
