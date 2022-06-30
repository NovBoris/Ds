while True:
    Reshenie = str(input('Введите S если хотите найти Площадь или P если хотите найти Периметр: '))
    print(Reshenie)
    if (Reshenie == 'S'):
        print('Найдем площадь прямоуголного треугольника через катеты:')
        Katet_1 = int(input('Введите первый катет треугольника: '))
        Katet_2 = int(input('Введите второй катет треугольника: '))
        print('S =', 0.5* (Katet_1 * Katet_2))
    elif (Reshenie == 'P'):
        print('Найдем периметр прямоуголного треугольника через сумму длин его сторон:')
        Katet_1 = int(input('Введите первый катет треугольника: '))
        Katet_2 = int(input('Введите второй катет треугольника: '))
        Gipotenyza = int(input('Введите гипотенузу: '))
        print('P =', Katet_1 + Katet_2 + Gipotenyza)
        break
    else:
        print('Выберите S или P')

