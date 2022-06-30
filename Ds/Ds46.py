# Создание папки для дз
# import os
# import shutil

# if not os.path.exists('Ds46'):
#     os.mkdir('Ds46')
# print(os.getcwd())
# os.chdir('Ds46')
# print(os.getcwd())

# 1. Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.

# task_list = ['First dfasbsdfbdf line', '1111', '4', '3', '2', '5', 'Second line_ab', '6', '9', '6', 7, 1, 'Third line_abcde']
#
# write_list = [[], []]
# for i in task_list:
#     if isinstance(i, int):
#         write_list[0].append(i)
#     elif i.isdigit():
#         write_list[0].append(int(i))
#     else:
#         write_list[1].append(i + ' ')
# write_list[0], write_list[1] = [str(x) + ' ' for x in sorted(write_list[0])], sorted(write_list[1], key=len)
#
# with open('Ds46_file_1.txt', 'w') as text_ds46_file_1:
#     text_ds46_file_1.writelines(write_list[1])
#     text_ds46_file_1.writelines(write_list[0])

# 2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

# with open('Ds46_file_2.txt', 'w', encoding='utf-8') as text_ds46_file_2:
#     while True:
#         text = input('Введите строку для записи в файл, или пустую строку для завершения программы: ') + '\n'
#         if text == '\n':
#             break
#         text_ds46_file_2.write(text)


# Удаление созданных файлов Дз

# os.remove('Ds46_file_1')
# os.remove('Ds46_file_2')
# os.chdir('..')
# os.rmdir('Ds46')

# Удаление папки с файлами

# os.chdir('..')
# shutil.rmtree('Ds46')

        