import sys, os
while 1==1:
    try:
        number_int_1 = int(input('Введите первое целое число: '))
        break
    except (ValueError):
        print('Но это не целое число(')
while 1==1:
    try:
        number_int_2 = int(input('Введите второе целое число: '))
        break
    except (ValueError):
        print('Но это не целое число(')
while 1==1:
    text_str = (input('Какое ваше любимое блюдо? '))
    if text_str.isalpha():
        print(text_str)
        break
    else:
        print('Это не блюдо(')
while 1==1:
    try:
        number_float_1 = float(input('Введите ваше любимое дробное число: '))
        break
    except (ValueError):
        print('Но это не число(')
print(text_str)
print(number_int_1+number_int_2+number_float_1)