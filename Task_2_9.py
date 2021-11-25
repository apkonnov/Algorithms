# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это
# число и сумму его цифр.

a = input('Введите числа через пробел ')
b = a.split(' ')
max_b = 0
max_sum = 0
for item in b:
    s = 0
    for ch in item:
        s += int(ch)
    if max_sum < s:
        max_sum = s
        max_b = item
print(f'число {max_b} с наибольшей суммой цифр = {max_sum}')
