import random


def create_mtrx(line, colmn, simp):
    mtrx = []
    for i in range(line):
        lst = []
        for j in range(colmn):
            lst.append(simp)
        mtrx.append(lst)
    return mtrx


P = create_mtrx(3, 3, "_")


def nise_print(lst):
    for el in lst:
        print(*el)


def goPlayer(Player1):
    go = ''
    while go != 'go':

        while True:
            try:
                in_line, in_column = list(map(int, (input('Введите строку и столбец: ').split())))
                print()
            except (TypeError, ValueError):
                print('Неверный формат')
                continue

            if in_line < 1 or in_line > 3 or in_column < 1 or in_column > 3:
                print('Выход за рамки')
            else:
                x, y = int(in_line) - 1, int(in_column) - 1
                break

        if P[x][y] == '_':
            P[x][y] = Player1

            go = 'go'
            nise_print(P)
            print()
            return x, y
        else:
            print('Эта плитка занята')


def goComp(symp):
    rng = 0
    go = ''

    while go != 'go':
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        if P[x][y] == '_':
            P[x][y] = symp
            go = 'go'
            nise_print(P)
            print()
        else:
            continue
        return x, y


def isFinish(x, y, symb):
    if (P[x][0] == P[x][1] == P[x][2] == symb) or (P[0][y] == P[1][y] == P[2][y] == symb) or (
            P[0][0] == P[1][1] == P[2][2] == symb) or (P[0][-1] == P[1][-2] == P[2][0] == symb):
        return 1
    else:
        return 0


def StartGame():
    Comp = ''
    while Comp == '':
        Player1 = input('Выберети свой знак + или 0: ')
        if Player1 == '+':
            Comp = '0'
        elif Player1 == '0':
            Comp = '+'
        else:
            print('Неверный символ')

    win = False
    count = len(P) * len(P[0])

    while win == False and count > 0:
        if Player1 == '+':
            count -= 1
            x, y = goPlayer(Player1)
            win += isFinish(x, y, Player1)

            if win == False and count > 0:
                count -= 1
                x, y = goComp(Comp)
                win += isFinish(x, y, Comp)

        elif Player1 == '0':
            count -= 1
            x, y = goComp(Comp)
            win += isFinish(x, y, Comp)

            if win == False and count > 0:
                count -= 1
                x, y = goPlayer(Player1)
                win += isFinish(x, y, Player1)

    print(f'Игра завершена выйграл {P[x][y]}' if win != False else 'Ничья')

StartGame()
