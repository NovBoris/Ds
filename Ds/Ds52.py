# 1. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.


# def simple_decore(fn):
#     def func(*args, **kwargs):
#         print('Start function')
#         print()
#         fn(*args, **kwargs)
#         print('End function')
#
#     return func
#
#
# @simple_decore
# def multifunction(*args):
#     for args_1 in args:
#         if isinstance(args_1, tuple):
#             total_length = 0
#             words = 0
#             print(f'Количество элементов в кортеже: {len(args_1)}')
#             for el_args in args_1:
#                 if isinstance(el_args, str):
#                     words += 1
#                     total_length += len(el_args)
#                     print(f'Слово: {el_args:<10} Длина слова: {len(str(el_args))}')
#             print(f'Количество слов в кортеже: {words}, Общая длина слов в кортеже: {total_length}')
#             print()
#
#         elif isinstance(args_1, list):
#             letters = 0
#             numbers = 0
#             print(f'Количество элементов в списке: {len(args_1)}')
#             for el_args in args_1:
#                 if isinstance(el_args, str):
#                     check_numbers = []
#                     check_letters = []
#                     if el_args.isdigit():
#                         numbers += 1
#                         print(f'Элемент: {el_args} строка, числа в ней: {el_args}, всего 1 число')
#                     else:
#                         if el_args.isalpha():
#                             print(f'Элемент: {el_args} строка, буквы в ней: {el_args}, всего {len(el_args)} букв(ы/а)')
#                         a = ''
#                         for b in el_args + ' ':
#                             if b.isdigit():
#                                 a += b
#                             elif not b.isdigit() and len(a) != 0:
#                                 numbers += 1
#                                 if b.isalpha():
#                                     check_letters.append(b)
#                                     letters += 1
#                                 check_numbers.append(a)
#                                 a = ''
#                             elif b.isalpha():
#                                 check_letters.append(b)
#                                 letters += 1
#                     if len(check_numbers) != 0:
#                         print(f'Элемент: {el_args} строка, буквы в ней: {check_letters},'
#                               f' всего {len(check_letters)} букв(ы/а)'
#                               f' числа в ней: {check_numbers}, '
#                               f' всего {len(check_numbers)} чис(ло/ла/ел)')
#                 else:
#                     numbers += 1
#                     print(f'Элемент: {el_args} число, 1 число')
#             print(f'Количество букв в списке: {letters}, Количество чисел в списке: {numbers}')
#             print()
#
#         elif isinstance(args_1, int):
#             res = [el_args for el_args in str(args_1) if int(el_args) % 2]
#             print(f'Количество нечетных цифр в числе {args_1} = {len(res)}, {res}')
#             print()
#
#         elif isinstance(args_1, float):
#             res = [el_args for el_args in str(args_1) if el_args.isdigit() and int(el_args) % 2]
#             print(f'Количество нечетных цифр в числе {args_1} = {len(res)}, {res}')
#             print()
#
#         elif isinstance(args_1, str):
#             res = [el_args for el_args in args_1 if el_args.isalpha()]
#             print(f'Количество букв в строке {args_1} = {len(res)}, {res}')
#             print()
#
# tuple_1 = ('sdbsb', 'abc', 'def', 123, 'vds')
# list_1 = ['s1d2b34s56d12b', '123', '673', 'abc', 'def', 123, 'vds1']
# int_1 = 1234567
# float_1 = 1234567.8901
# str_1 = 'a,b.c;defghij1234klm'
# simple_decore(multifunction(tuple_1, list_1, int_1, float_1, str_1))


#
# 2. Функцию которая при заданном целом числе n посчитает n + nn + nnn.
# from math import sqrt
#
#
# def sum_str_n(n):
#     n = str(n)
#     return int(n) + int(n + n) + int(n + n + n)
#
#
# def sum_int_n(n):
#     return n + (n+n) + (n+n+n)
#
#
# def multiplication_int_n(n):
#     return n + (n*n) + (n*n*n)
#
#
# def recursion_int_n(n, a=2):
#     if a == 0:
#         return n * sqrt(n)
#     return recursion_int_n(n * n, a - 1) + n
#
# print(f'5 + 55 + 555 = {sum_str_n(5)},\n5 + (5+5) + (5+5+5) = {sum_int_n(5)},\n'
#       f'5 + (5*5) + (5*5*5) = {multiplication_int_n(5)}\n')
#
# print(f'2 + (2 * 2) + (4 * 4 * 4) = {recursion_int_n(2)}')

# 3. Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

# from datetime import timedelta
#
#
# def time_in_seconds(seconds):
#     print(timedelta(seconds=seconds))
#
#
# def time_in_seconds_2(specified_seconds, choice):
#     if choice == 1:
#         seconds = specified_seconds
#         days = 0
#         hours = 0
#         minutes = 0
#         while seconds > 0:
#             if seconds // 86400 > 0:
#                 days += seconds // 86400
#                 seconds -= 86400 * (seconds // 86400)
#             elif seconds // 3600 > 0:
#                 hours += seconds // 3600
#                 seconds -= 3600 * (seconds // 3600)
#             elif seconds // 60 > 0:
#                 minutes += seconds // 60
#                 seconds -= 60 * (seconds // 60)
#             else:
#                 print(f'В {specified_seconds} секунд(дах/е): {days} Дней, {hours}:{minutes}:{seconds}')
#                 break
#     if choice == 2:
#         hours_seconds = specified_seconds
#         hours = 0
#         minutes = 0
#         while hours_seconds > 0:
#             if hours_seconds // 3600 > 0:
#                 hours += hours_seconds // 3600
#                 hours_seconds -= 3600 * (hours_seconds // 3600)
#             elif hours_seconds // 60 > 0:
#                 minutes += hours_seconds // 60
#                 hours_seconds -= 60 * (hours_seconds // 60)
#             else:
#                 print(f'В {specified_seconds} секунд(дах/е): {hours}:{minutes}:{hours_seconds}')
#                 break
#     if choice == 3:
#         minutes_seconds = specified_seconds
#         minutes = 0
#         while minutes_seconds > 0:
#             if minutes_seconds // 60 > 0:
#                 minutes += minutes_seconds // 60
#                 minutes_seconds -= 60 * (minutes_seconds // 60)
#             else:
#                 print(f'В {specified_seconds} секунд(дах/е): {minutes}:{minutes_seconds}')
#                 break
#
#
# time_in_seconds(int(input('Введите количество секунд: ')))
# time_in_seconds_2(int(input('Введите количество секунд: ')), int(input('1. Количество дней? 2. Часов? 3. Минут?: ')))
