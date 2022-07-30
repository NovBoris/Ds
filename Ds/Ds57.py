from random import randint
import sqlite3
import time


def int_game(player_name: str, count: str):
    start_time = time.time()
    player_count = 0
    win = True
    if count.isdigit():
        if int(count) > 10:
            print('Это много, я дам вам 10 попыток')
            count = 10
        elif int(count) < 1:
            print('Это мало, я дам вам 1 попытку')
            count = 3
        else:
            count = int(count)
            if count == 1:
                print(f'Хорошо, у тебя {count} попытка, это смело🧐')
            elif count in range(2, 5):
                print(f'У тебя {count} попытки')
            else:
                print(f'У тебя {count} попыток')
    else:
        print('Это не число')
        return
    number = randint(1, 10)
    print(number)
    for i in range(count):
        player_count += 1
        print('-------------------')
        if count == 1:
            print('Попытка всего 1, больше шансов не будет😈')
        elif i == 0:
            print('Первая попытка')
        elif count - i > 3:
            print(f'Попытка {i + 1}, шансов еще много🙄')
        elif count - i == 3:
            print(f'Попытка {i + 1}, я начинаю за тебя волноваться')
        elif count - i == 2:
            print(f'Попытка {i + 1}, правда, подумай хорошенько')
        elif count - i == 1:
            print(f'Попытка {i + 1}, последний шанс друг мой')
        try:
            player_number = int(input())
        except ValueError:
            print('Это не число')
            continue
        if number == player_number:
            if count == 1:
                print(f'Признаю, ты реально крут🤯. Ты сделал {player_count} попыток.')
                total_time = round((time.time() - start_time), 5)
                break
            elif count - i == 1:
                print(f'Я правда переживал, поздравляю, ты справился😤. Ты сделал {player_count} попыток.')
                total_time = round((time.time() - start_time), 5)
                break
            else:
                print(f'Поздравляю, ты победил😀. Ты сделал {player_count} попыток.')
                total_time = round((time.time() - start_time), 5)
                break
        elif number < player_number:
            print('-------------------'
                  '\nСлишком много')
        else:
            print('-------------------'
                  '\nСлишком мало')
        if count == 1:
            print('Ты конечно крут, но в этот раз переоценил себя, с 1 раза это что-то нереальное\n')
        elif i == 0:
            print('Первая для разогрева, дальше лучше\n')
        elif count - i > 3:
            print(f'Ничего страшного, все впереди\n')
        elif count - i == 3:
            print(f'Это сложнее чем кажется\n')
        elif count - i == 2:
            print(f'Еще есть шанс\n')
        elif count - i == 1:
            print(f'Ты старался, в следующий раз точно повезет\n')
    else:
        print(f'Ты проиграл😞. А число было {number}. Ты сделал {player_count} попыток.')
        win = False
        total_time = round((time.time() - start_time), 5)

    def data_base():
        with sqlite3.connect('LeaderBoard.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER,
            name TEXT,
            score INTEGER,
            time NUMERIC,
            PRIMARY KEY("id" AUTOINCREMENT)
            )""")
            if win:
                cur.execute("""INSERT INTO users (name, score, time) VALUES(?, ?, ?)""",
                            (player_name, player_count, total_time))
                # SELECT expressions
                # FROM tables
                # [WHERE conditions]
                # [ORDER BY expression[ASC | DESC]]
                # LIMIT number_rows[OFFSET offset_value];
            cur.execute("""SELECT name, score, time
                        FROM users
                        ORDER BY score, time ASC
                        LIMIT 3
                        """)
            result = cur.fetchall()
            print(f'Новая сортировка', result)
            cur.execute("""SELECT name, score, time
                        FROM users
                        ORDER BY score, time ASC
                        """)
            result = cur.fetchall()
            print(f'Список всех игроков', *result, sep='\n')
            cur.execute("SELECT * FROM users")
            result = cur.fetchall()
            print('Топ 3 игрока')
            [print(*sorted(result, key=lambda el: int(el[2]) and int(el[3]))[_][1:4]) for _ in range(3)]
    data_base()


int_game(input('Введите свое имя: '), input('Введите количество попыток (Минимум 1, Максимум 10): '))
