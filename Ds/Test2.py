#  Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке

# specified_list = [1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10]
# for i in specified_list:
#     if specified_list.count(i) > 1:
#         while i in specified_list:
#             specified_list.remove(i)
#         # print(i, end=' ')
# print(specified_list)


#  Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

# specified_list = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5]
# check_list = []
# for i in set(specified_list):
#     if specified_list.count(i) > 1:
#         print(f'Число пар {i} {specified_list.count(i) // 2}')
        # if specified_list.count(i) % 2 == 0 and i not in check_list:
        #     print(f'Число пар {i} {specified_list.count(i) // 2}')
        #     check_list.append(i)
        # elif specified_list.count(i) % 2 and i not in check_list:
        #     print(f'Число пар {i} {(specified_list.count(i) - 1) // 2}')
        #     check_list.append(i)

# import random
#
# list_spec = [random.randint(1, 5) for i in range(10)]
# print(list_spec)

# Даны два кортежа:

# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей

# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# print(f'Сумма больше в кортеже - "C_1"' if sum(C_1) > sum(C_2) else 'Сумма больше в кортеже - C_2')


#  Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

# specified_str = 'An apple a day keeps the doctor away'
# result_dict = {symbol: specified_str.count(symbol) for symbol in set(specified_str.replace(' ', ''))}
# print(result_dict)

# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания


# dict_2 = {'Торт': [5, 1000, ['Состав торта']],
#           'Пирожное': [2, 500, ['Состав пирожного']],
#           'Маффин': [3, 1000, ['Состав маффина']],
#           'Кекс': [4, 700, ['Состав кекса']],
#           'Хлеб': [2, 2000, ['Состав хлеба']],
#           'Чизкейк': [5, 1000, ['Состав чизкейка']],
#           'Безе': [5, 500, ['Состав безе']],
#           'Тирамису': [6, 1000, ['Состав тирамису']],
#           }
#
# end = ''
#
# def magazin(dict):
#     for i, v in dict.items():
#         print(f'Товар: {i:<10}Цена за 100гр: {v[0]:<5} В наличии {v[1]}гр')
#
# FinSum = 0
#
# while True:
#     end = input('Введите название товара, состав, цена, количество, вся информация или "n": ')
#     if end == 'n':
#         break
#     elif end == 'состав':
#         end_2 = input('Введите название товара: ')
#         if end_2 not in dict_2:
#             print('Такой позиции нет')
#             continue
#         else:
#             print(f'{end_2} {dict_2[end_2][2]}')
#             continue
#     elif end == 'цена':
#         end_2 = input('Введите название товара: ')
#         if end_2 not in dict_2:
#             print('Такой позиции нет')
#             continue
#         else:
#             print(f'{end_2} {dict_2[end_2][0]} за 100гр')
#             continue
#     elif end == 'количество':
#         end_2 = input('Введите название товара: ')
#         if end_2 not in dict_2:
#             print('Такой позиции нет')
#             continue
#         else:
#             print(f'{end_2} {dict_2[end_2][1]}гр')
#             continue
#     elif end == 'вся информация':
#         magazin(dict_2)
#         continue
#     elif end not in dict_2:
#         print('Такой позиции нет')
#         continue
#     while True:
#         try:
#             amount = int(input('Введите количество товара: '))
#             if dict_2.get(end)[1] >= amount:
#                 dict_2.get(end)[1] -= amount
#                 sum = dict_2.get(end)[0] * amount / 100
#                 FinSum += sum
#                 print(f'Сумма покупок {sum}\n')
#                 break
#             else:
#                 print('Недостаточно товара в магазине')
#                 print(f'Позиции {end} осталось {dict_2[end][1]}')
#         except (TypeError, ValueError):
#             print('Неверное значение')
#             continue
#
# print(f'\nСумма {FinSum}')
# print('До свидания')

#  Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.
# import random
#
# first_list = [random.randint(1, 15) for i in range(5)]
# second_list = [random.randint(1, 15) for i in range(5)]
# print(first_list, '\n', second_list)
# print(f'Списки содержат {len(set(first_list) & set(second_list))} одинаковых чис(ла/ел)')

# 7. Напишите программу, демонстрирующую работу try\except\finally

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

#  В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу

# import random
#
# Class_167 = ['Фам Лёша', 'Фам Паша', 'Фам Маша', 'Фам Даша', 'Фам Катя', 'Фам Лера', 'Фам Андрей']
# with open('Class_167', 'w', encoding='utf-8') as tabl:
#     for i in Class_167:
#         tabl.write(f'{i} {str(random.randint(0, 5))}\n')
#
# average_score = []
# while True:
#     with open('Class_167', encoding='utf-8') as text_pr:
#         for line in text_pr:
#             second_name, name, estimation = line.split()
#             average_score.append(int(estimation))
#             if int(estimation) < 3:
#                 print(f'У {second_name} {name} оценка < 3, оценка учащегося {estimation}')
#     print(f'Средний балл класса {(sum(average_score) / len(average_score)):,.3f}')


