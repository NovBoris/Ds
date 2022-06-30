print('----------------------------------------- Задание 6 -----------------------------------------------------------------')
Text = str(input('Введите слово: '))
print(Text)
Text = list(Text.replace(' ', ''))
num = 0
a = ''
res = 0
res_2 = 0
for i in Text:
    if a.islower() and i.islower():
        res += 1
    elif a.isupper() and i.isupper():
        res_2 += 1
    a = i
alf = ['a','e','i','o','u','y']
vowels = 0
list_vowels = []
consonants = 0
for i in Text:
    if i.lower() in alf:
        vowels += 1
        list_vowels.append(i)
    else:
        consonants += 1
print(f'В слове всего {len(Text)} букв\n{res} пар(ы) нижнего\n{res_2} пар(ы) верхнего\nГласных: {vowels}\nСогласных: {consonants}')