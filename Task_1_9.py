# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('1 число = '))
b = int(input('2 число = '))
c = int(input('3 число = '))
if b <= a <= c or c <= a <= b:
    print('средним является число ', a)
elif a <= b <= c or c <= b <= a:
    print('средним является число ', b)
elif a <= c <= b or b <= c <= a:
    print('средним является число ', c)
