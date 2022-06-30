# 1. Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность
#
# import random
#
# with open('input.txt', 'w+') as file_1:
#     for i in range(2):
#         file_1.write(f'{int(random.randint(0, 100))} ')
#     file_1.seek(0)
#     with open('output.txt', 'w') as file_2:
#         number_1, number_2 = file_1.readline().split()
#         file_2.write(f'{int(number_1) - int(number_2)}')


# Удаление
# from os import remove
# remove('input.txt')
# remove('output.txt')

# 2. В саду сорвали цветы
# На лугу сорвали цветы
# Создайте множество цветов, произрастающих одновременно в саду и на лугу

# garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# gar_and_mead_1 = set(set(garden).intersection(set(meadow)))
# gar_and_mead_2 = set(set(garden) & set(meadow))
# print(gar_and_mead_1)
# print(gar_and_mead_2)

# 3. Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова

# songsdict = {
# 'World in My Eyes': 4.76,
# 'Sweetest Perfection': 5.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.30,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6,
# 'Policy of Truth': 4.88,
# 'Blue Dress': 4.18,
# 'Clean': 5.68,
# }
# total_time_of_sound = 0
# sound_time_less5 = []
# one_word_songs = {}
# for k, v in songsdict.items():
#     total_time_of_sound += v
#     if v > 5:
#         sound_time_less5.append((k, v))
#     if len(k.split()) == 1:
#         one_word_songs[k] = v
# print(f'Общее время звучания всех песен: {total_time_of_sound}\n'
#       f'Список песен, время звучания которых больше 5 мин: {sound_time_less5}\n'
#       f'Словарь песен в названии которых 1 буква: {one_word_songs}')

