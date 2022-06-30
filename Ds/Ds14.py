Number_1 = float(input('Введите первое число: '))
Number_2 = float(input('Введите второе число: '))
Operation = input('Введите операцию: +, -, *, /, 0: ')
if Operation == '+' or Operation == '-' or Operation == '*' or Operation == '/' or Operation == '0':
    while Operation == '+' or Operation == '-' or Operation == '*' or Operation == '/' or Operation == '0':
        if Operation == '+':
            print(Number_1 + Number_2)
            break
        elif Operation == '-':
            print(Number_1 - Number_2)
            break
        elif Operation == '*':
            print(Number_1 * Number_2)
            break
        elif Operation == '/':
            if  Number_2 == 0:
                print('Нельзя делить на 0')
                break
            print(Number_1 / Number_2)
            break
        elif Operation == '0':
            print('Конец')
            break
else:
    print('Такой операции нет')
