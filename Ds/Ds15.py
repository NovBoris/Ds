import random
Number = random.randint(1,10)
Colour = random.randint(1,2)
if Colour == 1:
    Colour = 'красный'
elif Colour == 2:
    Colour = 'черный'
Attempt = 0
# print(f'{str(Number)} {Colour}')
while Attempt != 5:
    Answer =  input('Выберите число от 1 до 10 и цвет красный/черный: ')
    Attempt += 1
    if Answer == f'{str(Number)} {Colour}':
        print('Вы победили. Поздравляю!')
        break
else:
    print('Попытки закончили, вы проиграли.')
    print(f'{str(Number)} {Colour}')
