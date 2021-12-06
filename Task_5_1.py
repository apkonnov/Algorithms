# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections
import random
n = int(input('Введите количество предприятий '))
firms = []
firm = collections.namedtuple('Firm', ['name', 'kv1', 'kv2', 'kv3', 'kv4'])
for i in range(n):
    firms.append(firm(name='Фирма ' + str(i), kv1=random.random()*10000, kv2=random.random()*10000,
                      kv3=random.random()*10000, kv4=random.random()*10000))
s = 0
for item in firms:
    s += item.kv1 + item.kv2 + item.kv3 + item.kv4
avr = s / n
b = [item.name for item in firms if (item.kv1 + item.kv2 + item.kv3 + item.kv4) > avr]
c = [item.name for item in firms if (item.kv1 + item.kv2 + item.kv3 + item.kv4) < avr]

print('Прибыль больше средней у предприятий')
print(*b)
print('Прибыль меньше средней у предприятий')
print(*c)
