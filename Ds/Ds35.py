# 1. В вашем распоряжении имеется вложенный список people,
# в котором хранятся имена и телефоны.
# Ваша задача создать словарь при помощи генератора словарей,
# в котором в качестве ключей будут хранится номера телефонов,
# а значениями будут имена владельцев.

# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Ann Hoffman', '434.104.4302'],
#     ['John Leonard', '(956)182-8435'],
#     ['Daniel Ross', '870-365-8303x416'],
#     ['Jacqueline Moon', '+1-757-865-4488x652'],
#     ['Gregory Baker', '705-576-1122'],
#     ['Michael Spencer', '(922)816-0599x7007'],
#     ['Austin Vazquez', '399-813-8599'],
#     ['Chad Delgado', '979.908.8506x886'],
#     ['Jonathan Gilbert', '9577853541']
# ]
#
# print({i[1]: i[0] for i in people})

# print(dict((i[1], i[0]) for i in people))

# for i in people:
#     i.reverse()
# print(dict(i for i in people))

# for i in people:
#     i[0], i[1] = i[1], i[0]
# print(dict(i for i in people))


# 2. У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы. Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

# Dict_2 = {'Яйца': [2, 10],
#           'Молоко': [5, 10],
#           'Кефир': [3, 10],
#           'Масло': [4, 10],
#           'Творог': [2, 10],
#           'Сметана': [2, 10],
#           'Сыр': [5, 10],
#           'Йогурт': [6, 10],
#           'Мороженое': [2, 10],
#           'Молочные каши': [3, 10]
#           }
#
# end = ''
#
# def Magazin(Dict):
#     for i, v in Dict.items():
#         print(i, v[0], v[1], sep='-')
#
# Magazin(Dict_2)
#
# FinSum = 0
#
# while True:
#     end = input('Введите название товара: ')
#     if end == 'n':
#         break
#     elif end not in Dict_2:
#         print('Такой позиции нет')
#         continue
#     while True:
#         try:
#             amount = int(input('Введите количество товара: '))
#             if Dict_2.get(end)[1] >= amount:
#                 Dict_2.get(end)[1] -= amount
#                 sum = Dict_2.get(end)[0] * amount
#                 FinSum += sum
#                 print(f'Сумма покупок {sum}\n')
#                 break
#             else:
#                 print('Недостаточно товара в магазине')
#                 print(f'Позиции {end} осталось {Dict_2.get(end)[1]}')
#         except (TypeError, ValueError):
#             print('Неверное значение')
#             continue
#
# print(f'\nСумма {FinSum}\nОсталось товара:\n')
# Magazin(Dict_2)

# Dict_2 = {'Яйца': [2, 10],
#           'Молоко': [5, 10],
#           'Кефир': [3, 10],
#           'Масло': [4, 10],
#           'Творог': [2, 10],
#           'Сметана': [2, 10],
#           'Сыр': [5, 10],
#           'Йогурт': [6, 10],
#           'Мороженое': [2, 10],
#           'Молочные каши': [3, 10]
#           }
#
# end = ''
#
# def Magazin(Dict):
#     for i, v in Dict.items():
#         print(i, v[0], v[1], sep='-')
#
# Magazin(Dict_2)
#
# FinSum = 0
#
# while True:
#     end = input('Введите название товара или "n": ')
#     if end == 'n':
#         break
#     elif end not in Dict_2:
#         print('Такой позиции нет')
#         continue
#     while True:
#         try:
#             amount = int(input('Введите количество товара: '))
#             if Dict_2.get(end)[1] >= amount:
#                 Dict_2.get(end)[1] -= amount
#                 sum = Dict_2.get(end)[0] * amount
#                 FinSum += sum
#                 print(f'Сумма покупок {sum}\n')
#                 break
#             else:
#                 print('Недостаточно товара в магазине')
#                 print(f'Позиции {end} осталось {Dict_2[end][1]}')
#         except (TypeError, ValueError):
#             print('Неверное значение')
#             continue
#
# print(f'\nСумма {FinSum}\nОсталось товара:\n')
# Magazin(Dict_2)



# 3. Исправьте ошибки в коде, чтобы получить требуемый вывод. (Вывод True)


# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {'a': 300, 'b': 200, 'd':400}
#
# print(d1["b"] == d2["b"])

