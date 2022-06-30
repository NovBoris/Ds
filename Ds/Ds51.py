# 1. Написать функцию, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата. Сторону квадрата вводить с клавиатуры.
# from math import sqrt
#
# def square_characteristics(side):
#     if side.replace('.', '').isdigit():
#         side = float(side)
#         p = side * 4
#         s = side * side
#         d = side * sqrt(2)
#         return p, s, d
#     else:
#         return 'Это не число'
#
#
# print(square_characteristics(input('Введите сторону квадрата: ')))


# 2. Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


# def call_sum(a, b):
#     print(a + b)
#
#
# def call_minus(a, b):
#     print(a - b)
#
#
# def call_division(a, b):
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#
# def call_multiplication(a, b):
#     print(a * b)
#
#
# number_1 = float(input('Введите первое число: '))
# number_2 = float(input('Введите первое второе: '))
# operation = input('Введите операцию: +, -, /, * или 0 для завершения программы: ')
#
# if operation == '+':
#     call_sum(number_1, number_2)
# elif operation == '-':
#     call_minus(number_1, number_2)
# elif operation == '/':
#     call_division(number_1, number_2)
# elif operation == '*':
#     call_multiplication(number_1, number_2)
# elif operation == '0':
#     print('Программа завершена')
# else:
#     print('Такой операции нет')

# Учусь делать классы, можно по ним замечания? если есть.
# class Calculator:
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b
#
#     def call_sum(self):
#         print(self.a + self.b)
#
#     def call_minus(self):
#         print(self.a - self.b)
#
#     def call_division(self):
#         if self.b == 0:
#             print('На ноль делить нельзя')
#         else:
#             print(self.a / self.b)
#
#     def call_multiplication(self):
#         print(self.a * self.b)
#
#
# res = Calculator(5, 7)
# res.call_sum()
# res.call_minus()
# res.call_division()
# res.call_multiplication()


# 3. Напишите функцию, которая принимает на вход одно неотрицательное число,
# и возвращает значение факториала данного числа.

# from math import factorial
#
#
# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n - 1) * n
#
#
# print(fac(int(input('Факториал какого числа вы хотите узнать?: '))))
#
# a = int(input("Факториал какого числа вы хотите узнать?: "))
# print(f'Факториал числа {a}, это число {factorial(a)}')
