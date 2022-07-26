# 1. Игра угадай число. Компьютер загадывает число, от 1 до ста,
# задача пользователя угадать это число за определенное количество попыток.
# Компьютер сообщает по ходу игры, было ли введенное число меньше или больше загаданного.
# В случае когда попыток не осталось или пользователь выиграл, угадав число, получаем соответствующее сообщение.


# from random import randint
#
#
# def int_game(count: str):
#     if count.isdigit():
#         if int(count) > 10:
#             print('Это много, я дам вам 10 попыток')
#             count = 10
#         elif int(count) < 1:
#             print('Это мало, я дам вам 1 попытку')
#             count = 3
#         else:
#             count = int(count)
#             if count == 1:
#                 print(f'Хорошо, у тебя {count} попытка, это смело🧐')
#             elif count in range(2, 5):
#                 print(f'У тебя {count} попытки')
#             else:
#                 print(f'У тебя {count} попыток')
#     else:
#         print('Это не число')
#         return
#     number = randint(1, 10)
#     print(number)
#     for i in range(count):
#         print('-------------------')
#         if count == 1:
#             print('Попытка всего 1, больше шансов не будет😈')
#         elif i == 0:
#             print('Первая попытка')
#         elif count - i > 3:
#             print(f'Попытка {i + 1}, шансов еще много🙄')
#         elif count - i == 3:
#             print(f'Попытка {i + 1}, я начинаю за тебя волноваться')
#         elif count - i == 2:
#             print(f'Попытка {i + 1}, правда, подумай хорошенько')
#         elif count - i == 1:
#             print(f'Попытка {i + 1}, последний шанс друг мой')
#         try:
#             player_number = int(input())
#         except ValueError:
#             print('Это не число')
#             continue
#         if number == player_number:
#             if count == 1:
#                 print('Признаю, ты реально крут🤯')
#                 break
#             elif count - i == 1:
#                 print('Я правда переживал, поздравляю, ты справился😤')
#                 break
#             else:
#                 print('Поздравляю, ты победил😀')
#                 break
#         elif number < player_number:
#             print('-------------------'
#                   '\nСлишком много')
#         else:
#             print('-------------------'
#                   '\nСлишком мало')
#         if count == 1:
#             print('Ты конечно крут, но в этот раз переоценил себя, с 1 раза это что-то нереальное\n')
#         elif i == 0:
#             print('Первая для разогрева, дальше лучше\n')
#         elif count - i > 3:
#             print(f'Ничего страшного, все впереди\n')
#         elif count - i == 3:
#             print(f'Это сложнее чем кажется\n')
#         elif count - i == 2:
#             print(f'Еще есть шанс\n')
#         elif count - i == 1:
#             print(f'Ты старался, в следующий раз точно повезет\n')
#     else:
#         print(f'Ты проиграл😞. А число было {number}')
#
#
# int_game(input('Введите количество попыток (Минимум 1, Максимум 10): '))

# Конец первой задачи

# ----------------------------------------------------------------------------------------------------------------
# Вопрос
# Не могу разобраться почему выбивает ошибку, вроде если сразу записать номер страницы в url,
# то он на него заходит и все норм, но вторую страницу уже не открывает

# import requests
# from bs4 import BeautifulSoup
#
# for i in range(11):
#     if i == 0:
#         url = "https://www.kinoafisha.info/rating/movies/"
#     else:
#         url = f"https://www.kinoafisha.info/rating/movies/?page={i}"
#     print(url)
#     requests = requests.get(url)
#
#     soup = BeautifulSoup(requests.text, "html.parser")
#     cinema = []
#     teme = soup.find_all("a", class_="movieItem_title")
#     print(teme)
#     for temes in teme:
#         cinema.append(temes.text)
#
# print(cinema)
# ----------------------------------------------------------------------------------------------------------------

# Начало второй задачи

# Детская игра висилица. Аналог поле чудес, ток без барабана и секторов.
# Компьютер загадывает слово из списка слов, пользователь видит на экране это слово в виде звездочек за место букв
# и пытается угадать буквы, угаданная буква появляется вместо звездочки в слове.
# Можно усложнить наличием кол-ва попыток:)

# from random import choice
# from random_word import RandomWords
#
#
# def str_game():
#     car_brands = ['Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Lada', 'Mazda', 'MercedesBenz',
#                   'Mitsubishi', 'Nissan', 'Renault', 'Skoda', 'Toyota', 'Volkswagen']
#     words = ['Кант', 'Хроника', 'Зал', 'Галера', 'Балл', 'Вес', 'Кафель', 'Знак', 'Фильтр', 'Башня', 'Кондитер',
#              'Омар', 'Геолог', 'Бальзам', 'Бревно', 'Жердь', 'Борец', 'Самовар', 'Карабин', 'Подлокотник', 'Барак',
#              'Мотор', 'Шарж', 'Сустав', 'Амфитеатр', 'Скворечник', 'Подлодка', 'Затычка', 'Ресница', 'Спичка',
#              'Кабан', 'Муфта', 'Синоптик', 'Характер']
#     english_words = RandomWords()
#     choice_word = input('Какие слова хотите?: 1. Русские 2. Английские 3. Марки автомобилей (Eng): ')
#     try:
#         if int(choice_word) not in range(1, 4):
#             print('Такого варианта нет')
#             return
#         if choice_word == '1':
#             word = choice(words).lower()
#         elif choice_word == '3':
#             word = choice(car_brands).lower()
#         else:
#             word = (english_words.get_random_word()).lower()
#         print(word)
#         find_word = '*' * len(word)
#         missed_letters = []
#         correct_letters = []
#         win = False
#
#         def secret_word(s_word):
#             for i in range(len(word)):
#                 if word[i] in correct_letters:
#                     s_word = s_word[:i] + word[i] + s_word[i+1:]
#                     if '*' not in s_word:
#                         nonlocal win
#                         win = True
#             print(s_word)
#
#         choice_count = input('1. Хотите ввести количество попыток? 2. Или нет?: ')
#         if int(choice_count) not in range(1, 3):
#             print('Такого варианта нет')
#             return
#         elif choice_count == '1':
#             count = input('Введите количество попыток: ')
#             if count.isdigit():
#                 if int(count) > len(word) + 5:
#                     print(f'Это много, я думаю количество попыток должно быть таким: {len(word) + 5}')
#                     count = len(word) + 5
#                 elif int(count) < len(word):
#                     print(f'Это мало, я думаю количество попыток должно быть таким: {len(word)}')
#                     count = len(word)
#                 else:
#                     print(f'Количество попыток: {count}')
#                     count = int(count)
#             else:
#                 print('Это не число')
#                 return
#         else:
#             count = -1
#     except ValueError:
#         print('Такого варианта нет')
#         return
#     count_timer = count
#     print(f'Количество букв в слове {len(word)}')
#     secret_word(find_word)
#     while count > 0 or count < 0:
#         print('-------------------')
#         if count < 0:
#             print('Думай сколько хочешь. Или напиши стоп')
#         elif count_timer == count:
#             print(f'Ходов осталось {count_timer}')
#         elif count - count_timer == count - 1:
#             print(f'Ходов {count_timer}, последний шанс друг мой')
#         elif count > count_timer:
#             print(f'Ходов осталось {count_timer}, шансов еще много🙄')
#         player_letter = input('Введите букву: ').lower()
#         if player_letter == 'стоп':
#             print('Конец игры, в следующий раз точно угадаешь')
#             break
#         if player_letter in word:
#             if player_letter in correct_letters:
#                 print('Ты уже угадал эту букву')
#                 continue
#             correct_letters.append(player_letter)
#             secret_word(find_word)
#             print('Такая буква есть')
#             if win:
#                 print('Поздравляю, ты победил🤯')
#                 break
#             continue
#         elif player_letter in missed_letters:
#             print('-------------------'
#                   '\nЭта буква уже была')
#             print('Ты уже пропобовал', *missed_letters)
#             count_timer -= 1
#         else:
#             print('-------------------'
#                   '\nТакой буквы нет')
#             count_timer -= 1
#             missed_letters.append(player_letter)
#         if count_timer == 0:
#             print(f'Ты проиграл😞. А слово было {word}')
#             break
#
#
# str_game()

# Конец второй задачи
# ----------------------------------------------------------------------------------------------------------------


# Начало третьей задачи

# 3. Симулятор лифта. Суть в следующем, изначально консоль выдает сообщение,
# что вы на любом этаже (этажность придумываете сами) и предлагает ввести цифру этажа, чтобы подняться/спуститься,
# во время подема/спуска мы видим в принте проезжающие этажи (цифры). Доехав до нужного, мы получаем сообщение,
# где находимся и вновь (и так бесконечно или до кодового слова) мы можем спуститься или подняться на нужный этаж.
# В общем лифтик. Сложность еще и в том, что мы не можем опуститься ниже первого или подняться выше 10го
# (если в здании 10 этажей)


# from time import sleep
#
#
# class Elevator:
#     def __init__(self, floors=10):
#         self.floors = floors
#         self.elevator_floor = 1
#
#     def go_up_go_down(self, floor):
#         if floor > self.elevator_floor:
#             if floor > self.floors:
#                 floor = self.floors
#             for i in range(self.elevator_floor, floor + 1):
#                 print(f'Этаж {i}')
#                 sleep(1)
#             self.elevator_floor = floor
#         else:
#             if floor < 1:
#                 floor = 1
#             for i in range(self.elevator_floor, floor - 1, -1):
#                 print(f'Этаж {i}')
#                 sleep(1)
#             self.elevator_floor = floor
#
#     def __str__(self):
#         return f'Лифт сейчас на {self.elevator_floor} этаже'
#
#
# x = Elevator()
# print(x)
# x.go_up_go_down(6)
# x.go_up_go_down(15)
# x.go_up_go_down(-6)
# x.go_up_go_down(2)
# print(x.elevator_floor)


# Конец третей задачи
# ----------------------------------------------------------------------------------------------------------------


# Начало четвертой задачи

# 4. Создать класс мотоциклы. И минимум два экземпляра класса. У этих экземпляров помимо атрибутов есть методы.
# Это увелечение скорости, уменьшение скорости и цвет. Максимальная скорость у каждого обьекта разные,
# меньше нуля скорость уменьшаться не может. Все три атрибута приватные,
# т.е. мы не можем изменять параметры за пределами класса напрямую.
# По поводу методов скорости. Каждый раз вызывая метод увеличения скорости, скорость постоянно увеличивается от
# скорости заданной ранее вызванным методом (на энное кол-во км). Не заходя за максимум.
# Ну и уменьшение работает так же, только в обратную сторону.


# from time import sleep
#
#
# class Motorcycles:
#     __engine = 1
#     __wheels = 2
#     __frame = 1
#     __handlebar = 1
#
#     def __init__(self, max_speed, color):
#         self.__max_speed = max_speed
#         self.__color = color
#         self.__speed = 0
#
#     def increase_speed(self, speed):
#         if speed > self.__speed:
#             if speed > self.__max_speed:
#                 speed = self.__max_speed
#             for i in range(self.__speed, speed, 10):
#                 print(f'Скорость {i} км/ч')
#                 sleep(0.2)
#             self.__speed = speed
#
#     def slow_down(self, speed):
#         if speed < self.__speed:
#             if speed < 0:
#                 speed = 0
#             for i in range(self.__speed, speed, -30):
#                 print(f'Скорость {i} км/ч')
#                 sleep(0.2)
#             self.__speed = speed
#
#     def change_color(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f'Цвет {self.__color}. Скорость {self.__speed} км/ч'
#
#
# a = Motorcycles(250, 'red')
# b = Motorcycles(200, 'blue')
# print(a)
# a.increase_speed(152)
# a.slow_down(-4124)
# print(a)
# print(b)
# b.change_color('green')
# print(b)

# Конец четвертой задачи
