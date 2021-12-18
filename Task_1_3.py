# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

print(f'Уравнение прямой, проходящей через точки ({x1}, {y1}) и ({x2}, {y2})')
if x1 == x2 and y1 == y2:
    print('Одной точки мало')
elif x1 == x2:
    print(f'x = {x1:.2f}')
elif y1 == y2:
    print(f'y = {y1:.2f}')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    zn = '-' if b < 0 else '+'
    print(f'y = {k:.2f} x {zn} {abs(b):.2f}' if b != 0 else f'y = {k:.2f} x')
