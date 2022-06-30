# 1. Введите два числа с клавиатуры. Поделите одно на другое. Обработайте ошибку деления на ноль,
# если ошибок нет, то результат деления возвести в квадрат. Также используйте оператор finally.

# try:
#     number_1 = float(input('Введите первое число: '))
#     number_2 = float(input('Введите второе число: '))
#     number_3 = number_1 / number_2
#     print(number_3)
# except ValueError:
#     print('Вы ввели не числа')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(number_3 ** 2)
# finally:
#     print('Программа завершена')

# 2. Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.

# from numpy import *
#
# row = 5
# column = 5
# matrix = [[0] * column for i in range(row)]
# maximum = 0
#
# for b in range(column):
#     for c in range(row):
#         a = random.randint(1, 10)
#         matrix[b][c] = a
#     print(f'{matrix[b]} Сумма строки: {sum(matrix[b])}')
#     if maximum < sum(matrix[b]):
#         maximum = sum(matrix[b])
#         item = b + 1
# print(f'Номер максимальной строки {item}')
#
# # ---------------------------------------------------------
#
# a = arange(25).reshape(5, 5)
# print(a)

# 3. Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.

# while True:
#     try:
#         number_1 = float(input('Введите первое число: '))
#         number_2 = float(input('Введите второе число: '))
#         number_3 = number_1 / number_2
#         print(number_3)
#         break
#     except ValueError:
#         print('Вы ввели не числа')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')