import math

x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))
r = int(input('Введите радиус окружности: '))
c = x ** 2 + y ** 2
c = math.sqrt(c)
if r >= c:
    print('Точка принадлежит окружности')
else:
    print('Точка не принадлежит окружности')
