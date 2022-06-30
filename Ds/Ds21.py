lit = str(input('Введите букву: ').lower())
text = str(input('Введите предложение: '))
text_2 = list(text.split(' '))
list_res = []
for i in text_2:
    print(f'Сейчас слово: {text_2[0]}')
    if lit.lower() in i or lit.upper() in i:
        list_res.append(text_2[0])
    text_2 = text_2[1:]
print(list_res)
