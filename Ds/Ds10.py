Text = str(input('Введите строку: '))
print(Text)
Text2 = str(Text[::-1])
print(Text2)
Text = Text.lower().replace(' ','')
Text2 = str(Text[::-1])
Text2 = Text2.lower().replace(' ','')
if Text == Text2:
    print('Эта строка палиндром')
else:
    print('Эта строка не палиндром')