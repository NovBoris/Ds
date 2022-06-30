# age = input('Введите год: ')
# print(len(age))
# find_age = int(age) + 1
# if len(age) == 1:
#     print(find_age)
# else:
#     while len(set(str(find_age))) != len(age):
#         find_age += 1
#     print(find_age)
#
# year = int(input()) + 1
#
# while len(str(year)) != len(set(str(year))):
#     year += 1
# else:
#     print(year)

# text = input('Введите строку: ')
# print(list(set(text)))

# text = input('Введите строку: ')
# text_2 = ''
# for i in text:
#     if text.lower().count(i.lower()) == 1:
#         text_2 += i
#     else:
#         if i not in text_2:
#             text_2 += i
#
# print(text_2)

# text = input('Введите строку: ')
# text_2 = ''
# for i in text:
#     if text.count(i) == 1:
#         text_2 += i
# print(text_2)

text_3 = input('Введите строку: ')
for i in text_3:
    if text_3.count(i) == 1 or not i.isdigit():
        text_3 = text_3.replace(i, '')
print(text_3)
