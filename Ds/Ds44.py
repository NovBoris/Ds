# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

a = int(input())
list = {}
while a != 0:
    first_team, first_team_score, second_team, second_team_score = input().split(';')
    a -= 1
    if first_team not in list:
        list[first_team] = [0, 0, 0, 0, 0]
    if second_team not in list:
        list[second_team] = [0, 0, 0, 0, 0]

    if int(first_team_score) > int(second_team_score):
        list[first_team][1] += 1
        list[first_team][4] += 3
        list[second_team][3] += 1
    elif int(first_team_score) < int(second_team_score):
        list[second_team][1] += 1
        list[second_team][4] += 3
        list[first_team][3] += 1
    else:
        list[first_team][2] += 1
        list[first_team][4] += 1
        list[second_team][2] += 1
        list[second_team][4] += 1

    if first_team in list:
        list[first_team][0] += 1

    if second_team in list:
        list[second_team][0] += 1

for i, v in list.items():
    print(f'{i}:{" ".join(str(x) for x in v)}')

