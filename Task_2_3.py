# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

a = input('Введите натуральное число = ')
if a.isdigit():
    b = ''
    for ch in a:
        b = ch + b
    print(f'Исходное число {a}, обратное число {b}')
else:
    print('Вы ввели не натуральное число')
