Age = int(input('Введите год: '))

if Age%4==0 and Age%100!=0 or Age%400==0:
    print('Год високосный - 366 дней')
else:
    print('Год не високосный - 365 дней')

# Ages = []
# ages = 1995
# while ages < 2030:
#     ages = ages + 1
#     Ages.append(ages)
# for i in Ages:
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         print(i, '- Год високосный - 366 дней')
#     else:
#         print(i, '- Год не високосный - 365 дней')