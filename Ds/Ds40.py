# Удаление всех повторяющихся символов, включая регистры.

text = input('Введите строку: ')
text_2 = ''
for i in text:
    if text.lower().count(i.lower()) == 1:
        text_2 += i
print(text_2)

# Удаление всех повторяющихся символов, не включая регистры.

text = input('Введите строку: ')
text_2 = ''
for i in text:
    if text.count(i) == 1:
        text_2 += i
print(text_2)