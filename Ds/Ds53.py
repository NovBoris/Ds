# 1. Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

# class Calculator:
#     def __init__(self, a, b, operation=None):
#         self.a = a
#         self.b = b
#         self.operation = operation
#
#     def call(self):
#         if not self.a.isdigit() or not self.b.isdigit():
#             print('Вы ввели не числа')
#         elif self.b == '0' and '/' in self.operation:
#             print('На ноль делить нельзя')
#         elif self.operation is None or self.operation not in ['+', '-', '*', '**', '/', '//', '%']:
#             print('Такой операции нет')
#         else:
#             print(eval(self.a + self.operation + self.b))
#
#
# res = Calculator(input('Введите первое число: '),
#                  input('Введите второе число: '),
#                  input('Введите операцию: +, -, *, **, /, //, %\n'))
# res.call()

# ---------------------------------------------------------------------------------------------
# def call_sum(self):
#     print(self.a + self.b)
#
# def call_minus(self):
#     print(self.a - self.b)
#
# def call_division(self):
#     if self.b == 0:
#         print('На ноль делить нельзя')
#     else:
#         print(self.a / self.b)
#
# def call_multiplication(self):
#     print(self.a * self.b)

# res.call_sum()
# res.call_minus()
# res.call_division()
# res.call_multiplication()

# 2. Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.


# class String_or_number:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def let_or_num(self):
#         if self.arg.isdigit():
#             result = [int(i) for i in str(self.arg) if int(i) % 2 == 0]
#             print(sum(result) * len(str(self.arg)))
#         elif isinstance(self.arg, int):
#             result = [int(i) for i in str(self.arg) if int(i) % 2 == 0]
#             print(sum(result) * len(str(self.arg)))
#         elif isinstance(self.arg, str):
#             vowels = []
#             consonants = []
#             vowels_check = 'A, E, I, O, U, Y'
#             for i in self.arg:
#                 if i.isalpha():
#                     if i.upper() in vowels_check:
#                         vowels.append(i)
#                     else:
#                         consonants.append(i)
#             if len(vowels) * len(consonants) <= len(self.arg.replace(' ', '')):
#                 print(vowels)
#             else:
#                 print(consonants)
#
#
# test_1 = String_or_number(input())
# test_1.let_or_num()
