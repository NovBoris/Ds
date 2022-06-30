# ----------------------------------------- Задание 1 -----------------------------------------------------------------

# print('----------------------------------------- Задание 1 -----------------------------------------------------------------')
# Number = list(input('Введите 7 значное число: '))
# even = 0
# odd = 0
# sum = 0
# if len(Number) == 7:
#     for i in Number:
#         sum += int(i)
#         odd_res = int(Number[0]) * int(Number[2]) * int(Number[5])
#         if int(i) % 2 == 0:
#             even += 1
#         else:
#             odd += 1
# else:
#     print('Это не 7 значное число')
# if even > odd:
#     print(sum)
# else:
#     print(odd_res)
#
# # ----------------------------------------- Задание 2 -----------------------------------------------------------------
#
# print('----------------------------------------- Задание 2 -----------------------------------------------------------------')
# import string
# print(string.punctuation)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# Text = str(input('Введите текст: '))
# alf = ['a','e','i','o','u','y']
# vowels = 0
# list_vowels = []
# consonants = 0
# for i in Text.strip():
#     if i.lower() in alf:
#         vowels += 1
#         list_vowels.append(i)
#     elif i in string.ascii_lowercase:
#         consonants += 1
# print(f'Гласных: {vowels}\nСогласных: {consonants}')
# if vowels == consonants:
#     print(list_vowels)
#
# # ----------------------------------------- Задание 3 -----------------------------------------------------------------
#
# import random
#
# print('----------------------------------------- Задание 3 -----------------------------------------------------------------')
# Number1 = int(input('Введите первое число: '))
# Number2 = int(input('Введите второе число: '))
# Attempt = 0
# more = 0
# less = 0
# Res = 0
# if Number1 < 1 or Number1 > 20 or Number2 < 1 or Number2 > 20:
#     print('Числа должны быть от 1 до 20')
# else:
#     while Attempt !=7:
#         RanNumber1 = random.randint(1, 20)
#         RanNumber2 = random.randint(1, 20)
#         if (Number1 + Number2) > (RanNumber1 + RanNumber2):
#             more += 1
#         elif (Number1 + Number2) < (RanNumber1 + RanNumber2):
#             less += 1
#         else:
#             Res += 1
#         if Attempt == 4:
#             Ran_Number_Res = f'{RanNumber1}, {RanNumber2}'
#         Attempt += 1
#     print(f'Ваша пара была {more} раз(а) больше\nВаша пара была {less} раз(а) меньше')
#     if Res > 0:
#         print(f'Ваша пара была равна моей паре {Res} раз(а)\n4 итерация: {Ran_Number_Res}')
#
# # ----------------------------------------- Задание 4 -----------------------------------------------------------------
#
# print('----------------------------------------- Задание 4 -----------------------------------------------------------------')
# import random
# Number = int(input('Из скольки цифр будет состоять число?: '))
# LookNumber = int(input('Какую цифру искать?: '))
# Numbers_list = []
# for i in range(Number):
#     Numbers_list.append(random.randint(1,100))
# print(Numbers_list)
# print(Numbers_list.count(LookNumber))
#
# # ----------------------------------------- Задание 5 -----------------------------------------------------------------
#
# print('----------------------------------------- Задание 5 -----------------------------------------------------------------')
# import string
# print(string.digits)
# print(type(string.digits))
#
# Text = input('Введите любую строку: ')
# for a in Text:
#     if a not in string.digits:
#         Text = Text.replace(a, '')
# print(' '.join(Text.split()))
#
# for a in Text:
#     if a.isdigit():
#         print(a, end=' ')
# print()
# Text = Text.split()
# for i in Text:
#     if i.isdigit():
#         print(i, end=' ')
#
# # ----------------------------------------- Задание 6 -----------------------------------------------------------------
#
# # print('----------------------------------------- Задание 6 -----------------------------------------------------------------')
# Text = str(input('Введите слово: '))
# print(Text)
# Text = list(Text.replace(' ', ''))
# num = 0
# a = ''
# res = 0
# res_2 = 0
# for i in Text:
#     if a.islower() and i.islower():
#         res += 1
#     elif a.isupper() and i.isupper():
#         res_2 += 1
#     a = i
# alf = ['a','e','i','o','u','y']
# vowels = 0
# list_vowels = []
# consonants = 0
# for i in Text:
#     if i.lower() in alf:
#         vowels += 1
#         list_vowels.append(i)
#     else:
#         consonants += 1
# print(f'В слове всего {len(Text)} букв\n{res} пар(ы) нижнего\n{res_2} пар(ы) верхнего\nГласных: {vowels}\nСогласных: {consonants}')
