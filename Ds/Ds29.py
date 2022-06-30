# t = ("+79123456", "+78123456", "+77123456", "+59123456", "+39123456", "+76123456")
# print([i for i in t if '+7' in i])

# n = 'Оценки: 5,4,3,4,2,4,5,4'
# print(tuple(map(int, ([i for i in n if i.isdigit()]))))

# b = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# for i in b:
#     i = (', '.join(list(map(str, list(i))))).replace(',', ' -')
#     print(i)

# def Ploshad(a, b):
#     S = 1/2 * a * b
#     return S
#
# print(Ploshad(4, 7))

# def PorS(a, b, c):
#     if c == 'S':
#         Res = 1/2 * a * b
#     else:
#         Res = (a + b) * 2
#     return Res
#
# print(PorS(5, 5, 'S'))

# a = list(map(int, input().split()))
# a = input().split()
# print(max(a))
# print(a)
# def Max(a):
#     if (', '.join(a)).isdigit():
#         a = list(map(int, a))
#         return max(a)
#     else:
#         return max(a)
#
# print(a, Max(a), a)

# a = input().split()
# a = list(map(int, a))
# def Max(a):
#     sum = 1
#     for i in a:
#         sum *= i
#     return sum
#
# print(Max(a))

# a = ['0','0','0']
# b = ['0','0','0']
# c = ['0','0','0']
# f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
# status = True
# print(f)
# def Player1(x):
#     if x == 0:
#         if y == 0:
#             a[0] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 1:
#             a[1] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 2:
#             a[2] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#     elif x == 1:
#         if y == 0:
#             b[0] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 1:
#             b[1] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 2:
#             b[2] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#     elif x == 2:
#         if y == 0:
#             c[0] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 1:
#             c[1] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 2:
#             c[2] = '1'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
# def Player2(x):
#     if x == 0:
#         if y == 0:
#             a[0] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 1:
#             a[1] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 2:
#             a[2] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#     elif x == 1:
#         if y == 0:
#             b[0] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 1:
#             b[1] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 2:
#             b[2] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#     elif x == 2:
#         if y == 0:
#             c[0] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 1:
#             c[1] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
#         elif y == 2:
#             c[2] = '2'
#             f = (f'{"  ".join(a)}\n{"  ".join(b)}\n{"  ".join(c)}')
#             return f
# while status:
#     x,y = input().split()
#     x = int(x) - 1
#     y = int(y) - 1
#     print(Player1(x))
#     print(Player2(x))

import random


def create_mtrx(line, colmn, symb):
    """ Создание двумерного массива (поля),
    заполненного указанными символами
    """
    mtrx = []
    for i in range(line):
        internal = []
        for j in range(colmn):
            internal.append(symb)
        mtrx.append(internal)
    return mtrx


F = create_mtrx(3, 3, "_")  # Игровое поле глобальная переменная


def nice_print(lst):
    """(Вывод двумерного массива в виде матрицы),
    Функция отображения текущего состояния поля.
    """
    for el in lst:
        print(*el)


def goPlayer(symb):
    gou = ""
    while gou != "go":

        (in_line, in_column) = input("введите строку (1-3), столбик(1-3): ").replace(",", " ").split()
        x, y = int(in_line) - 1, int(in_column) - 1

        if x not in range(0, 3) or y not in range(0, 3):
            print("\nНеверные координаты\n")
        else:
            if F[x][y] == "_":
                F[x][y] = symb

                gou = "go"
                nice_print(F)
                print()
                return x, y

            else:
                print("\nЭта клетка занята!\n")


def goComp(symb):
    rng = random.Random()
    gou = ""

    while gou != "go":
        x = rng.randrange(len(F))
        y = rng.randrange(len(F[0]))

        if F[x][y] != "_":
            continue
        else:
            F[x][y] = symb
            gou = "go"
            nice_print(F)
            print()
    return x, y


def ifFinish(x, y, symb):
    if (F[x][0] == F[x][1] == F[x][2] == symb) or (F[0][y] == F[1][y] == F[2][y] == symb) or (
            F[0][0] == F[1][1] == F[2][2] == symb) or (F[0][-1] == F[1][-2] == F[2][0] == symb):
        return 1
    else:
        return 0


def createGame():
    """Создание игрового поля, распределение
    фишек - игрок выбирает крестик или нолик,
    первый ход, если компьютеру достался крестик
    """
    symb = input("Выберите свой символ + или 0 (ноль): ")
    comp = "+" if symb == "0" else "0"

    win = False
    count = len(F) * len(F[0])

    while win == False and count > 0:
        if symb == "+":
            count -= 1
            x, y = goPlayer(symb)
            win += ifFinish(x, y, symb)

            if win == False and count > 0:
                count -= 1
                x, y = goComp(comp)
                win += ifFinish(x, y, comp)

        if symb == "0":
            count -= 1
            x, y = goComp(comp)
            win += ifFinish(x, y, symb=comp)

            if win == False and count > 0:
                count -= 1
                x, y = goPlayer(symb)
                win += ifFinish(x, y, symb)

    print("Игра окончена, выиграл %s" % F[x][y]) if win != False else print("Боевая ничья")


createGame()

