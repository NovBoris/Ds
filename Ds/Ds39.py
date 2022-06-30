# x = int(input())
# y = int(input())
# z = int(input())
# print((x + z) // 60 + y)
# print((x + z) % 60)

# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)

# a = True
# b = False
# print(a and b or not a and not b)

# x = int(input())
# y = int(input())
# z = int(input())
# if z < x:
#     print('Недосып')
# elif z <= y:
#     print('Это нормально')
# else:
#     print('Недосып')

# x = int(input())
# if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
#     print('Високосный')
# else:
#     print('Обычный')

# print("123" + "42")

# x = int(input())
# y = int(input())
# z = int(input())
# import math
# p = (x + y + z) / 2
# print(math.sqrt(p * (p - x)*(p - y)*(p - z)))

# x = int(input())
# if x in range(-15, 12) or x in range(14, 17) or x >= 19:
#     print(True)
# else:
#     print(False)

# print([x for x in range(14, 18)])
# import math
#
# x = input()
# if x == 'треугольник':
#     c = int(input())
#     y = int(input())
#     z = int(input())
#     p = (c + y + z) / 2
#     print(math.sqrt(p * (p - c)*(p - y)*(p - z)))
# elif x == 'прямоугольник':
#     c = int(input())
#     y = int(input())
#     print(c * y)
# elif x == 'круг':
#     z = int(input())
#     print(3.14 * math.pow(z, 2))

# c = int(input())
# y = int(input())
# z = int(input())
# list = [c, y, z]
# list.sort()
# print(f'{list[-1]}\n{list[0]}\n{list[1]}')

# c = int(input())
# if c in range(11, 1001, 100) or c in range(12, 1001, 100) or c in range(13, 1001, 100) or c in range(14, 1001, 100):
#     print(f'{c} программистов')
# elif c == 1 or c in range(21, 1001, 10):
#     print(f'{c} программист')
# elif c == 2 or c == 3 or c == 4 or c in range(22, 1001, 10) or c in range(23, 1001, 10) or c in range(24, 1001, 10):
#     print(f'{c} программиста')
# else:
#     print(f'{c} программистов')

# i = list(range(0, 1000))
# for c in i:
#     if c in range(11, 1001, 100) or c in range(12, 1001, 100) or c in range(13, 1001, 100) or c in range(14, 1001, 100):
#         print(f'{c} программистов')
#     elif c == 1 or c in range(21, 1001, 10):
#         print(f'{c} программист')
#     elif c == 2 or c == 3 or c == 4 or c in range(22, 1001, 10) or c in range(23, 1001, 10) or c in range(24, 1001, 10):
#         print(f'{c} программиста')
#     else:
#         print(f'{c} программистов')

# c = input()
# if (int(c[0]) + int(c[1]) + int(c[2])) == (int(c[-1]) + int(c[-2]) + int(c[-3])):
#     print('Счастливый')
# else:
#     print('Обычный')

# i = 0
# while i <= 10:
#     i = i + 1
#     print(i)
#     if i > 7:
#         i = i + 2
# print(i)

# a = int(input())
# sum = 0
# while a != 0:
#     sum += a
#     a = int(input())
# print(sum)
#
# a = int(input())
# b = int(input())
# while b != 0:
#     if a < b:
#         a, b = b, a
#     a, b = b, (a % b)
# print(a)

# a = int(input())
# b = int(input())
# d = 0
# while True:
#     d += 1
#     if d % a == 0 and d % b == 0:
#         print(d)
#         break

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

# a = int(input())
# while a <= 100:
#     if a >= 10:
#         print(a)
#     a = int(input())


# a = int(input())
# c = int(input())
# y = int(input())
# z = int(input())
#
# if y > 10:
#     y = 10
# if z > 10:
#     z = 10
# if a > 10:
#     a = 10
# if c > 10:
#     c = 10
# if y == z:
#     print(f'\t{y}', end='')
# else:
#     for i in range(y, z + 1):
#         print(f'\t{i}', end='')
# print()
# for i in range(a, c + 1):
#     if a == c:
#         print(f'{i}', end='')
#         for z in range(y, z + 1):
#             print(f'\t{z * i}', end='')
#         print()
#     else:
#         print(f'{i}', end='')
#         for z in range(y, z + 1):
#             print(f'\t{z * i}', end='')
#         print()

# a = int(input())
# c = int(input())
# sum = 0
# n = 0
# for i in range(a, c + 1):
#     if i % 3 == 0:
#         sum += i
#         n += 1
# print(sum / n)

# a, b = int(input()), int(input())
# a += -a % 3
# print(a)
# b -= b % 3
# print(b)
# print((a + b) / 2)
